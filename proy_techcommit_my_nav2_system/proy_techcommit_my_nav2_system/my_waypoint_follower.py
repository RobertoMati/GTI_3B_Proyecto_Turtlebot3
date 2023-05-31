import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped, Vector3

from nav2_msgs.action import FollowWaypoints


class WaypointFollower(Node):
    def __init__(self):
        super().__init__('waypoint_follower')
        self._action_client = ActionClient(
            self, FollowWaypoints, 'follow_waypoints')
        self.waypoints = []

        self.subscription = self.create_subscription(
            Vector3,
            '/follow_waypoints',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # las coordenadas que tenemos se pasan a waypoints
        waypoint = PoseStamped()
        waypoint.header.frame_id = 'map'
        waypoint.pose.position.x = msg.x
        waypoint.pose.position.y = msg.y
        waypoint.pose.orientation.z = 0.0
        waypoint.pose.orientation.w = 1.0
        self.waypoints.append(waypoint)

        # envia el waypoint cada vez que se forma uno
        self.send_waypoints()

    def send_waypoints(self):
        self._action_client.wait_for_server()

        self.get_logger().info('Acción activa :)')

        goal_pose = FollowWaypoints.Goal()

        goal_pose.poses = self.waypoints
        self._action_client.wait_for_server()
        self.get_logger().info('Acción activa :)')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_pose,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)
        self.get_logger().info('Goal lanzado :)')

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.missed_waypoints))
        self.waypoints.clear()  # borra la lista de los waypoints porque si se anyaden nuevos volvera a los anteriores y luego a los nuevos que ha recibido


def main(args=None):
    rclpy.init(args=args)
    waypoint_follower = WaypointFollower()
    rclpy.spin(waypoint_follower)


if __name__ == '__main__':
    main()