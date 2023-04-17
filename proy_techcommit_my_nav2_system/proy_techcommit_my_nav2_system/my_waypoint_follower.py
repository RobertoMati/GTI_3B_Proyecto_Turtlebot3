import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped

class WaypointFollower(Node):
    def __init__(self):
        super().__init__('waypoint_follower')
        self.client = ActionClient(self, NavigateToPose, 'NavigateToPose')
        self.waypoints = self.define_waypoints()

    def define_waypoints(self):
        # Definir una lista de waypoints como objetos de tipo PoseStamped
        waypoints = []
        # Agregar waypoints a la lista en el formato deseado
                # Waypoint 1
        waypoint1 = PoseStamped()
        waypoint1.header.frame_id = 'map'
        waypoint1.pose.position.x = 1.0
        waypoint1.pose.position.y = 2.0
        waypoint1.pose.orientation.z = 0.0
        waypoint1.pose.orientation.w = 1.0
        waypoints.append(waypoint1)

    # Waypoint 2
        waypoint2 = PoseStamped()
        waypoint2.header.frame_id = 'map'
        waypoint2.pose.position.x = 3.0
        waypoint2.pose.position.y = 4.0
        waypoint2.pose.orientation.z = 0.0
        waypoint2.pose.orientation.w = 1.0
        waypoints.append(waypoint2)

    # Waypoint 3
        waypoint3 = PoseStamped()
        waypoint3.header.frame_id = 'map'
        waypoint3.pose.position.x = 5.0
        waypoint3.pose.position.y = 6.0
        waypoint3.pose.orientation.z = 0.0
        waypoint3.pose.orientation.w = 1.0
        waypoints.append(waypoint3)

    # Waypoint 4
        waypoint4 = PoseStamped()
        waypoint4.header.frame_id = 'map'
        waypoint4.pose.position.x = 7.0
        waypoint4.pose.position.y = 8.0
        waypoint4.pose.orientation.z = 0.0
        waypoint4.pose.orientation.w = 1.0
        waypoints.append(waypoint4)

    # Waypoint 5
        waypoint5 = PoseStamped()
        waypoint5.header.frame_id = 'map'
        waypoint5.pose.position.x = 9.0
        waypoint5.pose.position.y = 10.0
        waypoint5.pose.orientation.z = 0.0
        waypoint5.pose.orientation.w = 1.0
        waypoints.append(waypoint5)

   
        return waypoints

    def send_waypoints(self):
    # Enviar la lista de waypoints al servidor de la acción
        for waypoint in self.waypoints:
            goal = NavigateToPose.Goal()
            goal.pose = waypoint
            self.client.wait_for_server()
            future = self.client.send_goal_async(goal)

def main(args=None):
    rclpy.init(args=args)
    waypoint_follower = WaypointFollower()
    waypoint_follower.send_waypoints()
    rclpy.spin(waypoint_follower)
    waypoint_follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()