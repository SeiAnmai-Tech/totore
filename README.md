# toto_simulation_ros2

Go to terminal and run:
1. `sudo apt install git -y`
2. `mkdir -p ~/ros2_ws/src`
3. `cd ~/ros2_ws/src`
4. `git clone <SSH_Key_of_github_repo> -b humble`
5. `cd toto_simulation_ros2/`
6. `chmod +x install.sh`
7. `./install.sh`

**Important:**

Now follow these steps:
1. Open a new terminal and run `gazebo`.
2. Go to the "Insert" tab at the top of left bar.
3. From the drop-down menu of your "GAZEBO_MODEL_PATH" directory, add `toto2` and `TOTO House` to the gazebo environment.
4. After this, you can close Gazebo.

**Gazebo Simulations:**

1. Run `ros2 launch toto2_description simulation.launch.py` to launch Gazebo and RViz.
2. Run `ros2 run toto2_teleop teleop_keyboard` to control TOTO using your keyboard **OR** run `ros2 launch toto2_description joystick.launch.py` to control using PS4 controller.

**SLAM:** 

1. Run `ros2 launch toto2_description nav2.launch.py slam:=True`.
2. For keyboard control, run `ros2 run toto2_teleop teleop_keyboard` **OR** run `ros2 launch toto2_description joystick.launch.py` to control using PS4 controller.
3. To save your map, run to `cd ros2_ws/src/toto_simulation_ros2/toto2_description/maps/` and then to save map run `ros2 run nav2_map_server map_saver_cli -f ~/{name_of_your_map}`

**Navigation:**

**If you are using your own map**, follow these steps before starting the Navigation Stack:

1. Change `static_map_path = os.path.join(pkg_share, 'maps', 'house.yaml')` to `static_map_path = os.path.join(pkg_share, 'maps', '{name_of_your_map}.yaml')` in **/toto2_description/launch/nav2.launch.py**.
2. Change `default_value=os.path.join(map_dir, 'maps', 'house.yaml')` to `default_value=os.path.join(map_dir, 'maps', '{name_of_your_map}.yaml')` in **/toto2_navigation/launch/localization.launch.py**.
3. Change `yaml_filename: "house.yaml"` to `yaml_filename: "{name_of_your_map}.yaml"` in **/toto2_navigation/params/toto2_nav2_params.yaml**.

To launch the navigation stack:

1. Run `ros2 launch toto2_description nav2.launch.py`.
2. Click the **2D Pose Estimate button** in the RViz2 menu. (Position of the robot will be near outside wall and below main gate of the house).
3. Click on the map where the robot is located in gazebo and drag the large green arrow toward the direction where the robot is facing.
4. After this, click the **Navigation2 Goal** button in the RViz2 menu.
5. Click on the map to set the destination of the robot and drag the green arrow toward the direction where the robot will be facing.

Waypoint Navigation:

1. Run `ros2 launch toto2_description nav2.launch.py`.
2. Click the **2D Pose Estimate** button in the RViz2 menu. (Position of the robot will be near outside wall and below main gate of the house).
3. Now click the **Waypoint mode** button in the bottom left corner of RViz. Clicking this button puts the system in waypoint follower mode.
4. Click **Navigation2 Goal** button, and click on areas of the map where you would like your robot to go (i.e. select your waypoints). Select as many waypoints as you want.
5. When you’re ready for the robot to follow the waypoints, click the **Start Navigation** button in the bottom left corner of RViz.

**Note:** 
* This green arrow is a marker that can specify the destination of the robot.
* The root of the arrow is x, y coordinate of the destination, and the angle θ is determined by the orientation of the arrow.
* As soon as x, y, θ are set, TOTO will start moving to the destination immediately.
