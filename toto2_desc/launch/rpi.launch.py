from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Create a list to hold all the launch actions
    ld = LaunchDescription()

    # Add the first command: docker run -it --rm -v /dev:/dev --privileged --net=host microros/micro-ros-agent:humble serial --dev /dev/ttyACM0 -b 115200
    # docker_command = ExecuteProcess(
    #     cmd=['docker', 'run', '-it', '--rm', '-v', '/dev:/dev', '--privileged', '--net=host', 'microros/micro-ros-agent:humble', 'serial', '--dev', '/dev/ttyACM0', '-b', '115200']
    # )
    # ld.add_action(docker_command)

    # Add the second command: ros2 launch toto2_desc slam.launch.py
    ros2_command = ExecuteProcess(
        cmd=['ros2', 'launch', 'toto2_desc', 'slam.launch.py']
    )
    ld.add_action(ros2_command)

    # Add the third command: ros2 launch rplidar_ros rplidar.launch.py
    rplidar_command = ExecuteProcess(
        cmd=['ros2', 'launch', 'rplidar_ros', 'rplidar.launch.py']
    )
    ld.add_action(rplidar_command)

    return ld

if __name__ == '__main__':
    generate_launch_description()
