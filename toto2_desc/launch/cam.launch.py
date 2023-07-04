from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Create a list to hold all the launch actions
    ld = LaunchDescription()

    # Add the first command: ros2 launch toto2_cam demo_launch.py
    rplidar_command = ExecuteProcess(
        cmd=['ros2', 'launch', 'toto2_cam', 'demo_launch.py']
    )
    ld.add_action(rplidar_command)

    # Add the second command: ros2 launch aruco_ros double.launch.py
    rplidar_command = ExecuteProcess(
        cmd=['ros2', 'launch', 'aruco_ros', 'double.launch.py']
    )
    ld.add_action(rplidar_command)

    return ld

if __name__ == '__main__':
    generate_launch_description()
