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

    # Add the third command: ros2 run py_pubsub servo_state
    servo_state_node = Node(
        package='py_pubsub',
        executable='servo_state'
    )
    ld.add_action(servo_state_node)

    return ld

if __name__ == '__main__':
    generate_launch_description()
