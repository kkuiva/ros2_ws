#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MappingNode(Node):
    def __init__(self):
        super().__init__("mapping_node")
        self.get_logger().info("Mapping node started")

        #liikumiskäskude saatja
        self._pose_publisher = self.create_publisher(Twist, "/cmd_vel", 10)

        #LiDARi mõõtmiste vastuvõtja
        self._scan_listener = self.create_subscription(LaserScan, "/scan", self.robot_controller, 10)

    def robot_controller(self, scan: LaserScan):
        move_command = Twist()
        n = 20  #muutuja, mis lihtsustab suunavahemike määramist

        #määrab, millised LiDARi mõõtmised (suunad) kuuluvad mingisse gruppi (ees, taga, vasakul, paremal)
        self.front = min(scan.ranges[:n-1] + scan.ranges[-n:])
        self.left = min(scan.ranges[90-n:90+n])
        self.back = min(scan.ranges[180-n:180+n])
        self.right = min(scan.ranges[290-n:290+n])

        if self.front < 0.5: #kui ees on takistus
            if self.right <= 0.7: #ja paremal on sein
                move_command.linear.x = 0.05    
                move_command.angular.z = 0.5    #keerab vasakule
            else:   #kui paremal ei ole seina
                move_command.linear.x = 0.05
                move_command.angular.z = -0.4   #keerab paremale

        elif self.right > 0.35:  #kui paremal ei ole seina
                move_command.linear.x = 0.1
                move_command.angular.z = -0.5   #keerab paremale

        else:   #kui robot on seina ääres ja takistusi ei ole ees
            move_command.linear.x = 0.3     #liigub otse

        #liikumiskäskude saatmine
        self._pose_publisher.publish(move_command)

def main(args=None):
    rclpy.init(args=args)
    node = MappingNode()
    rclpy.spin(node)
    rclpy.shutdown()