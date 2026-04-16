To start the autonomous mapping, you need to open three terminals and run the following commands:

1. Launch the simulated environment in Gazebo:
    ros2 launch my_robot_controller turtlebot3_world.launch.py

2. Launch the mapping:
    ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True

3. Run the mapping movement script:
    ros2 run my_robot_controller mapping

The robot will try to follow the wall anti-clockwise to go through the entire environment.