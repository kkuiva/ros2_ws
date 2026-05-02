To start autonomous mapping of a world, you must first specify the world file name and path in src/my_robot_controller/launch/turtlebot3_world.launch.py.
(Depending on the world, you may also need to adjust the robot's spawn location in the same file)

After changing the file, you must save the files, build and source the workspace. 

To run the mapping, you can use the following command in your workspace:
ros2 launch my_robot_controller mapping.launch.py

This will launch Gazebo, which simulates the robot and the world, and Rviz, which displays the mapping process. It will also start the robot movement script, which makes the robot move around in the world by following the wall to its right. 

Once the world has been fully mapped, the map can be saved using the following command in another terminal:
(Before running the command, double check that the directory "~/ws/src/my_robot_controller/map" and the filename "my_map" are correct)
ros2 run nav2_map_server map_saver_cli -f ~/ws/src/my_robot_controller/map/my_map 


In order to run navigation in the mapped environment, you can use the following command:
ros2 launch my_robot_controller navigation.launch.py

To change the world and map being used: 
1. The world file in src/my_robot_controller/launch/turtlebot3_world.launch.py must be changed to the desired world file. 
2. The map file defined in src/my_robot_controller/launch/navigation.launch.py must be changed to the corresponding map file. 
2.1. You must check that the origin point of the coordinates in Gazebo matches the one in Rviz. If not, you must adjust the map file's origin by the robot's offset from the Gazebo origin coordinates. 
3. Set the robot's initial position in turtlebot3_world.launch.py and navigation.py according to the environment used.
4. Change the goal positions in navigation.py according to the environment used.