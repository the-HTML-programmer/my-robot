#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusPublisherNode(Node):   
    """
    A ROS2 node that publishes hardware status messages at regular intervals.

    This node is responsible for periodically publishing the status of hardware components
    to the 'hardware_status' topic using the `HardwareStatus` message type. It is intended
    to be used as a monitoring component within a ROS2 system, providing real-time updates
    about the hardware's operational state.

    Attributes:
        hardware_status_publisher (Publisher): The ROS2 publisher object used to send
            `HardwareStatus` messages on the 'hardware_status' topic.
        timer (Timer): A ROS2 timer that triggers the periodic execution of the
            `publish_status` method.
    
    Methods:
        __init__():
            Initializes the node, sets up the publisher and timer, and logs a startup message.
        publish_status():
            Callback function executed by the timer. Constructs a `HardwareStatus` message,
            sets its fields (e.g., `are_motors_ready`, `debug_message`), and publishes it
            to the 'hardware_status' topic.
    """
    def __init__(self):
        super().__init__("hardware_status_publisher") 
        self.hardware_status_publisher = self.create_publisher(
            HardwareStatus, "hardware_status", 10)
        self.timer = self.create_timer(1.0, self.publish_status)
        self.get_logger().info("hardware status publisher has been started")


    def publish_status(self):
        msg = HardwareStatus()
        # msg.temperature = 49.5
        msg.are_motors_ready = True
        msg.debug_message = "nothing serious"
        self.hardware_status_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args) 
    node = HardwareStatusPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
