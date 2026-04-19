To start autonomous mapping of a world, you must first specify the world file name and path in src/my_robot_controller/launch/turtlebot3_world.launch.py.
(Depending on the world, you may also need to adjust the robot's spawn location in the same file)

After changing the file, you must save the files, build and source the workspace. 

To run the mapping, you can use the following command in your workspace:
ros2 launch my_robot_controller mapping.launch.py

This will launch Gazebo, which simulates the robot and the world, and Rviz, which displays the mapping process. It will also start the robot movement script, which makes the robot move around in the world by following the wall to its right. 

Once the world has been fully mapped, the map can be saved using the following command in another terminal:
(Before running the command, double check that the directory "~/ws/src/my_robot_controller/map" and the filename "my_map" are correct)
ros2 run nav2_map_server map_saver_cli -f ~/ws/src/my_robot_controller/map/my_map 