ros2 run demo_nodes_cpp talker
rviz
rviz2
exit
ros2 run demo_nodes_cpp listener
rqt_graph 
exit
. build_ws.sh
exit
ros2 topic list
ros2 topic info /turtle1/cmd_vel
ros2 interface show geometry_msgs/msg/Twist
exit
clear
ls
ros2 run turtlesim turtlesim_node
exit
. build_ws.sh 
cd src/
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
cd src/
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
cd ..
ls
cd
exit
ros2 node list
rqt graph
rqt_graph 
. build_ws.sh 
ros2 launch my_robot_controller draw_circle.launch.py 
cd src/my_robot_controller/my_robot_controller/
touch turtle_controller.py
chmod +x turtle_controller.py 
cd
cd ws/
. build_ws.sh 
ros2 run turtlesim_nose
ros2 run my_robot_controller turtle_controller
source ~/ros2_ws/install/setup.bash
source ~/install/setup.bash
. build_ws.sh 
ros2 run turtlesim turtlesim_node 
. build_ws.sh 
ros2 run my_robot_controller turtle_controller.launch.py
ros2 run my_robot_controller turtle_controller 
. build_ws.sh 
ros2 run my_robot_controller turtle_controller.launch.py
. build_ws.sh 
ros2 run my_robot_controller turtle_controller.launch.py
. build_ws.sh 
ros2 run my_robot_controller turtle_controller.launch.py
chmod -x turtle_controller.launch.py
cd src
ros2 run my_robot_controller turtle_controller.launch.py
cd my_robot_controller/
touch launch/turtle_controller.launch.py 
cd ..
ros2 run my_robot_controller turtle_controller.launch.py
cd ..
ros2 run my_robot_controller turtle_controller.launch.py
cd src/my_robot_controller/
ros2 run my_robot_controller turtle_controller.launch.py
cd ..
exit
git submodule add -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git src/turtlebot3_simulations
exit
. build_ws.sh 
exit
. build_ws.sh 
ls
cd src
ls
rm -rf turtlebot3_simulations/
ls
cd ..
rm -rf .git/modules/src/turtlebot3_simulations/
cd
. build_ws.sh 
cd ws
. build_ws.sh 
ros2 launch my_robot_controller turtlebot3_world.launch.py 
gazebo
. build_ws.sh 
ros2 launch my_robot_controller turtlebot3_world.launch.py 
gazebo
. build_ws.sh 
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/ws/src/my_robot_controller/map/map.yaml
. build_ws.sh 
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/ws/src/my_robot_controller/map/map.yaml
source install/setup.bash 
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/ws/src/my_robot_controller/map/map.yaml
. build_ws.sh 
ros2 launch my_robot_controller turtlebot3_navigation.launch.py
. build_ws.sh 
ros2 launch my_robot_controller turtlebot3_navigation.launch.py
