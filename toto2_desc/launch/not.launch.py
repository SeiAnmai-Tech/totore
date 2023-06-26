from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Create a list to hold all the launch actions
    ld = LaunchDescription()

    # Add the first command: ros2 run py_pubsub converstor
    convertor_node = Node(
        package='py_pubsub',
        executable='convertor'
    )
    ld.add_action(convertor_node)

    # Add the second command: ros2 run py_pubsub odom
    odom_node = Node(
        package='py_pubsub',
        executable='odom'
    )
    ld.add_action(odom_node)

    # Add the third command: ros2 launch rplidar_ros view_rplidar.launch.py
    # view_rplidar_node = ExecuteProcess(
    #     cmd=['ros2', 'launch', 'rplidar_ros', 'view_rplidar.launch.py']
    # )
    # ld.add_action(view_rplidar_node)

    # Add the fourth command: ros2 launch toto2_desc nav2.launch.py
    view_robot_node = ExecuteProcess(
        cmd=['ros2', 'launch', 'toto2_desc', 'nav2.launch.py']
    )
    ld.add_action(view_robot_node)

    return ld

if __name__ == '__main__':
    generate_launch_description()
