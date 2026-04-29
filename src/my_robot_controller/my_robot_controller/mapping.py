#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MappingNode(Node):
    def __init__(self):
        super().__init__("mapping_node")
        self.get_logger().info("Mapping node started")

        #movement command publisher
        self._pose_publisher = self.create_publisher(Twist, "/cmd_vel", 10)

        #LiDAR measurement subscriber
        self._scan_listener = self.create_subscription(LaserScan, "/scan", self.robot_controller, 10)

    def robot_controller(self, scan: LaserScan):
        move_command = Twist()
        n = 20  #variable to simplify setting measurement ranges

        #defines which measurements belong in which sector (front, back, left, right) and gets the minimum measurement in each sector
        self.front = min(scan.ranges[:n-1] + scan.ranges[-n:])
        self.left = min(scan.ranges[90-n:90+n])
        self.back = min(scan.ranges[180-n:180+n])
        self.right = min(scan.ranges[290-n:290+n])

        if self.front < 0.5: #if there is an obstacle ahead
            if self.right <= 0.7: #and a wall/obstacle on the right
                move_command.linear.x = 0.05    
                move_command.angular.z = 0.5    #turn left
            else:   #if there is no wall/obstacle on the right
                move_command.linear.x = 0.05
                move_command.angular.z = -0.4   #turn right

        elif self.right > 0.35:  #(if there is no obstacle ahead) and the robot isn't close enough to the wall on the right
                move_command.linear.x = 0.1
                move_command.angular.z = -0.5   #turn right

        else:   #(if there is no obstacle ahead and the robot is close enough to the wall on the right)
            move_command.linear.x = 0.3     #drive straight ahead

        #sending movement commands to the robot
        self._pose_publisher.publish(move_command)

def main(args=None):
    rclpy.init(args=args)
    node = MappingNode()
    rclpy.spin(node)
    rclpy.shutdown()