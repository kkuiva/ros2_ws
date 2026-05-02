#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
import tf_transformations
import math
import time

class TurtleNavigationNode(Node):
    def __init__(self):
        super().__init__("navigation")
        self.get_logger().info("Navigation Node started")

        self.goal_poses = [  #defining the goal positions, I added the positions and changed ’yaw’ to ’z_rot’ and ’w_rot’
            {'x': 2.127, 'y': -4.824, 'z_rot': -0.163, 'w_rot': 0.987},
            {'x': 2.557, 'y': -1.532, 'z_rot': 0.993, 'w_rot': 0.119},
            {'x': -2.675, 'y': -4.306, 'z_rot': 0.757, 'w_rot': 0.653},
            {'x': -1.164, 'y': -1.252, 'z_rot': 1.0, 'w_rot': 0.003},
            {'x': -4.08, 'y': -1.436, 'z_rot': 0.937, 'w_rot': 0.348},
            {'x': -5.876, 'y': -2.546, 'z_rot': -0.598, 'w_rot': 0.801},
            {'x': -5.496, 'y': -4.692, 'z_rot': 0.188, 'w_rot': 0.982},
            {'x': -0.994, 'y': -2.478, 'z_rot': 0.705, 'w_rot': 0.709}
        ]

        self.current_goal_index = 0

        #publishers to publish initial position and the goal positions
        self.initial_pose_publisher = self.create_publisher(
            PoseWithCovarianceStamped, "/initialpose", 10)
        self.goal_pose_publisher = self.create_publisher(
            PoseStamped, "/goal_pose", 10)

        #subscriber for receiving robot’s position
        self.odom_listener = self.create_subscription(
            Odometry, "/odom", self.odom_callback, 10)
            
        time.sleep(5) # wait to let the simulation and turtlebot navigation to being loaded.
        self.publish_initial_pose() #publishing robot’s initial position
        time.sleep(5)
        self.publish_goal() #publishing first goal

    def publish_initial_pose(self):
        initial_pose = PoseWithCovarianceStamped() #defines message type
        #adds data to the message
        initial_pose.header.frame_id = 'map'
        initial_pose.pose.pose.position.x = -1.0
        initial_pose.pose.pose.position.y = -2.5

        quaternion = tf_transformations.quaternion_from_euler(0, 0, 0)
        initial_pose.pose.pose.orientation.x = quaternion[0]
        initial_pose.pose.pose.orientation.y = quaternion[1]
        initial_pose.pose.pose.orientation.z = quaternion[2]
        initial_pose.pose.pose.orientation.w = quaternion[3]

        self.initial_pose_publisher.publish(initial_pose) #publishes the initial position

    def odom_callback(self, msg: Odometry): #function that is called when an /odom message is received
        current_pose = msg.pose.pose
        goal_pose = self.goal_poses[self.current_goal_index]

        distance_to_goal = math.sqrt( #calculates the distance between robot position and goal
            (current_pose.position.x - goal_pose['x']) ** 2 +
            (current_pose.position.y - goal_pose['y']) ** 2
        )

        if distance_to_goal < 0.3: #if the robot is close enough to the goal
            self.publish_next_goal() #publish the next goal

    def publish_next_goal(self): 
        if self.current_goal_index < len(self.goal_poses) - 1: #checks if there is a goal left
            self.current_goal_index += 1 #increases the index to start using the next goal
            self.publish_goal() #publishes the new goal
        else:
            self.get_logger().info("All goals reached!")
            rclpy.shutdown()

    def publish_goal(self):
        #accesses the position information of the current goal
        goal = self.goal_poses[self.current_goal_index]
        pose_msg = PoseStamped() #defines message type
		#adds data to the message
        pose_msg.header.frame_id = 'map'
        pose_msg.pose.position.x = goal['x']
        pose_msg.pose.position.y = goal['y']
   
        #removed the following line because the points I used had rotation in quaternions
		#quaternion = tf_transformations.quaternion_from_euler(0, 0, math.radians(goal[’yaw’])) 

        pose_msg.pose.orientation.x = 0.0 #quaterion[0] in example code
        pose_msg.pose.orientation.y = 0.0 #quaterion[1] in example code
        pose_msg.pose.orientation.z = goal['z_rot'] #quaterion[2] in example code
        pose_msg.pose.orientation.w = goal['w_rot'] #quaterion[3] in example code

        time.sleep(0.5)
        self.goal_pose_publisher.publish(pose_msg) #publishes the goal
        self.get_logger().info(f"Published goal {self.current_goal_index + 1}")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleNavigationNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Navigation Node stopped")
    finally:
        rclpy.shutdown()