import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # config = os.path.join(
    #     get_package_share_directory('py_param_tutorial'), 'config', 'params.yaml'
    # )
    
    parking_node = Node(
        package = 'py_topic_tutorial',
        executable = 'strsub_cmdpub',
        name = 'topiclaunch_example',
        output='screen',
        # parameters = [config]
    )


    return LaunchDescription([
        parking_node
    ])