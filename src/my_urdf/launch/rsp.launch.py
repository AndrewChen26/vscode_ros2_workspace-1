from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro

def generate_launch_description():
    # Get the package directory
    package_dir = get_package_share_directory('my_urdf')

    # Path to the xacro file
    xacro_file = os.path.join(package_dir, 'description', 'simple_urdf.xacro')

    # Ensure the file exists
    if not os.path.exists(xacro_file):
        raise FileNotFoundError(f"Xacro file '{xacro_file}' does not exist.")

    # Process the xacro file
    robot_description = xacro.process_file(xacro_file).toxml()

    # Define the robot_state_publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # Return the launch description
    return LaunchDescription([
        robot_state_publisher_node
    ])
