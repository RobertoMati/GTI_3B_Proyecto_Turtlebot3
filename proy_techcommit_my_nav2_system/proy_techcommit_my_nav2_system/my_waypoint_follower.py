import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
import time

#from nav2_msgs.action import NavigateToPose

# El tipo de mensaje es FollowWaypoints

from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped

class WaypointFollower(Node):
    def __init__(self):
        super().__init__('waypoint_follower')
        
        #self.client = ActionClient(self, NavigateToPose, 'NavigateToPose')
        self._action_client = ActionClient(self, FollowWaypoints, 'follow_waypoints')
        
        self.waypoints = self.define_waypoints()

    def define_waypoints(self):
        # Definir una lista de waypoints como objetos de tipo PoseStamped
        waypoints = []
        # Agregar waypoints a la lista en el formato deseado
        # Waypoint 2
        waypoint2 = PoseStamped()
        waypoint2.header.frame_id = 'map'
        waypoint2.pose.position.x = -9.6
        waypoint2.pose.position.y = 3.71
        waypoint2.pose.orientation.z = 0.0
        waypoint2.pose.orientation.w = 1.0
        waypoints.append(waypoint2)
        # Waypoint 3
        waypoint3 = PoseStamped()
        waypoint3.header.frame_id = 'map'
        waypoint3.pose.position.x = -19.7
        waypoint3.pose.position.y = -7.94
        waypoint3.pose.orientation.z = 0.0
        waypoint3.pose.orientation.w = 1.0
        waypoints.append(waypoint3)
        
    # Waypoint 4
        waypoint4 = PoseStamped()
        waypoint4.header.frame_id = 'map'
        waypoint4.pose.position.x = -17.5
        waypoint4.pose.position.y = -3.54
        waypoint4.pose.orientation.z = 0.0
        waypoint4.pose.orientation.w = 1.0
        waypoints.append(waypoint4)
        # Waypoint 4_5
        waypoint4_5 = PoseStamped()
        waypoint4_5.header.frame_id = 'map'
        waypoint4_5.pose.position.x = -16.1
        waypoint4_5.pose.position.y = -7.31
        waypoint4_5.pose.orientation.z = 0.0
        waypoint4_5.pose.orientation.w = 1.0
        waypoints.append(waypoint4_5)

    # Waypoint 5
        waypoint5 = PoseStamped()
        waypoint5.header.frame_id = 'map'
        waypoint5.pose.position.x = -10.2
        waypoint5.pose.position.y = -15.6
        waypoint5.pose.orientation.z = 0.0
        waypoint5.pose.orientation.w = 1.0
        waypoints.append(waypoint5)
    # Waypoint 6
        waypoint6 = PoseStamped()
        waypoint6.header.frame_id = 'map'
        waypoint6.pose.position.x = -10.2
        waypoint6.pose.position.y = -12.7
        waypoint6.pose.orientation.z = 0.0
        waypoint6.pose.orientation.w = 1.0
        waypoints.append(waypoint6)
        # Waypoint 7
        waypoint7 = PoseStamped()
        waypoint7.header.frame_id = 'map'
        waypoint7.pose.position.x = 1.66
        waypoint7.pose.position.y = -9.01
        waypoint7.pose.orientation.z = 0.0
        waypoint7.pose.orientation.w = 1.0
        waypoints.append(waypoint7)
        # Waypoint 8
        waypoint8 = PoseStamped()
        waypoint8.header.frame_id = 'map'
        waypoint8.pose.position.x = 1.28
        waypoint8.pose.position.y = -11.1
        waypoint8.pose.orientation.z = 0.0
        waypoint8.pose.orientation.w = 1.0
        waypoints.append(waypoint8)
   
        return waypoints

    def send_waypoints(self):
    # Enviar la lista de waypoints al servidor de la acción
        #for waypoint in self.waypoints:
        #    goal = NavigateToPose.Goal()
        #    goal.pose = waypoint
        #    self.client.wait_for_server()
        #    future = self.client.send_goal_async(goal)
    # Enviar todos los waypoints a la vez
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
        #self.get_logger().info('Received feedback: {0}'.format(feedback.feedback))

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    #definimos la funcion de respuesta al resultado
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.missed_waypoints))
        time.sleep(1)
        # Cerrar el nodo y llamar a rclpy.shutdown() después de recibir el resultado de la acción
        self.destroy_node()
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    waypoint_follower = WaypointFollower()
    waypoint_follower.send_waypoints()
    rclpy.spin(waypoint_follower)
    waypoint_follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()