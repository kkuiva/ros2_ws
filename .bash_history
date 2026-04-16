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
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
ros2 run turtlesim turtlesim_node
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
colcon build
gazebo
exit
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener
ros2 run turtlesim turtle_teleop_key
exit
colcon build
cd
exit
colcon build
exit
. build_ws.sh
ls
cd src
ls
cd turtlebot3
ls
cd ..
cd .. 
. build_ws.sh
ls
cd src
rm turtlebot3
git submodule add -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git src/turtlebot3_simulations
. build_ws.sh 
exit
source /opt/ros/humble/setup.bash
exit
. build_ws.sh 
colcon build
ls
docker build --no-cache --progress=plain .
exit
ls
. build_ws.sh 
ln -sf /usr/share/zoneinfo/Europe/Tallinn /etc/localtime
sudo ln -sf /usr/share/zoneinfo/Europe/Tallinn /etc/localtime
export TZ=Europe/Tallinn
. build_ws.sh 
docker exec -it <43236394e193> ls -ld log
docker exec -it 43236394e193 ls -ld log
exit
. build_ws.sh 
ros2 run turtlebot3_teleop teleop_keyboard 
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
source ~/install/setup.bash
source ~/.bashrc
. build_ws.sh 
ros2 topic list
ros2 topic echo /cmd_vel
ros2 launch turtlebot3_bringup rviz2.launch.py
ros2 run turtlebot3_teleop teleop_keyboard 
. build_ws.sh 
ros2 run my_robot_controller mapping
source install/setup.bash
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
. build_ws.sh 
ros2 run my_robot_controller mapping
