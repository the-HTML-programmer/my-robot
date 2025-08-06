#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


"""
number_publisher.py

This module defines the NumberPublisherNode class, a ROS2 node that periodically publishes a specified integer value to the 'number' topic.
"""
class NumberPublisherNode(Node):
    """
    A ROS2 node that periodically publishes an integer value to the 'number' topic.

    Attributes:
        number (int): The integer value to publish.
        timer_period (float): The interval in seconds between publishes.
        number_publisher (Publisher): The ROS2 publisher for the 'number' topic.
        timer (Timer): The ROS2 timer that triggers periodic publishing.
    """

    def __init__(self):
        """
        Initializes the NumberPublisherNode, declares parameters, creates the publisher and timer, and logs startup.
        """
        super().__init__("number_publisher")
        self.declare_parameter("number", 2)
        self.declare_parameter("timer_period", 1.0)
        self.number = self.get_parameter("number").value
        self.timer_period = self.get_parameter("timer_period").value
        self.number_publisher = self.create_publisher(Int64, "number", 10)
        self.timer = self.create_timer(self.timer_period, self.callback_number_publisher)
        self.get_logger().info("number publisher has been started")

    def callback_number_publisher(self):
        """
        Callback function that publishes the configured integer value to the 'number' topic.
        """
        msg = Int64()
        msg.data = self.number
        self.number_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args) 
    node = NumberPublisherNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
