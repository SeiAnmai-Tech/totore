# toto2

Before running this repo, make sure your toto2 simulation is working. (https://github.com/SeiAnmai-Tech/toto_simulation_ros2/tree/srikrishna-humble)

Go to terminal and run:
1. `sudo apt install git -y`
2. `mkdir -p ~/ros2_ws/src`
3. `cd ~/ros2_ws/src`
4. `git clone <SSH_Key_of_github_repo>`
5. `cd toto2/`

**Keyboard controls:** 
1. `ros2 run toto2_teleop keyboard`.
2. 

**Run these commands everytime:** 
1. `ros2 run py_pubsub pico_reset`
2. `docker run -it --rm -v /dev:/dev --privileged --net=host microros/micro-ros-agent:humble serial --dev /dev/ttyACM0 -b 115200`
3. `docker run -it --rm -v /dev:/dev --privileged --net=host microros/micro-ros-agent:humble serial --dev /dev/ttyACM1 -b 115200`
4. `ros2 launch toto2_desc everything.launch.py`

**To run camera:**
1. Run `ros2 launch toto2_cam demo_launch.py`. 
2. Then, in your PC run `ros2 run rqt_image_view rqt_image_view` to see camera's output.

**To run ArUco:**
1. Run `ros2 launch aruco_ros double.launch.py` (OR) launch camera and aruco using `ros2 launch toto2_desc cam.launch.py`. 

**To Dock autonomously:**
1. Run camera and ArUco first and then run `ros2 run py_pubsub gotodock`.

**SLAM:** 

1. Run `ros2 launch toto2_desc nav2.launch.py slam:=True`.
2. For keyboard control, run `ros2 run toto2_teleop keyboard` **OR** run `ros2 launch toto2_desc joystick.launch.py` to control using PS4 controller in your PC.
3. To save your map run `ros2 run nav2_map_server map_saver_cli -f ~/{name_of_your_map}` in your PC.

**Navigation:**

**If you are using your own map**, follow these steps before starting the Navigation Stack:

1. Change `static_map_path = os.path.join(pkg_share, 'maps', 'house.yaml')` to `static_map_path = os.path.join(pkg_share, 'maps', '{name_of_your_map}.yaml')` in **/toto2_desc/launch/nav2.launch.py**.
2. Change `default_value=os.path.join(map_dir, 'maps', 'house.yaml')` to `default_value=os.path.join(map_dir, 'maps', '{name_of_your_map}.yaml')` in **/toto2_nav/launch/localization.launch.py**.
3. Change `yaml_filename: "house.yaml"` to `yaml_filename: "{name_of_your_map}.yaml"` in **/toto2_nav/params/toto2_nav2_params.yaml**.

To launch the navigation stack:

1. Run `ros2 launch toto2_desc nav2.launch.py`.
2. Now run `ros2 launch toto2_nav rviz_launch.py` in your PC and click the **Set 2D Pose Estimate** button in the RViz2 menu and set robot's initial position.
3. After this, click the **Navigation2 Goal** button in the RViz2 menu.
4. Click on the map to set the destination of the robot and drag the green arrow toward the direction where the robot will be facing.

Waypoint Navigation:

1. Run `ros2 launch toto2_desc nav2.launch.py`.
2. Now run `ros2 launch toto2_nav rviz_launch.py` in your PC and click the **Set 2D Pose Estimate** button in the RViz2 menu and set robot's initial position.
3. Click **Navigation2 Goal** button, and click on areas of the map where you would like your robot to go (i.e. select your waypoints). Select as many waypoints as you want.
5. When you’re ready for the robot to follow the waypoints, click the **Start Navigation** button in the bottom left corner of RViz.

**Note:** 
* This green arrow is a marker that can specify the destination of the robot.
* The root of the arrow is x, y coordinate of the destination, and the angle θ is determined by the orientation of the arrow.
* As soon as x, y, θ are set, TOTO will start moving to the destination immediately.
