#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node):  
    """
    A ROS2 node that subscribes to the 'robot_news' topic and logs incoming messages.

    This node is intended to simulate a smartphone device that receives news updates from a robot.
    Upon initialization, it creates a subscription to the 'robot_news' topic, expecting messages of type `String`.
    Whenever a new message is received, the `callback_robot_news` method is triggered, which logs the content of the message.

    Attributes:
        suscriber (Subscription): The subscription object for the 'robot_news' topic.

    Methods:
        __init__():
            Initializes the SmartphoneNode, sets up the subscription, and logs a startup message.
        callback_robot_news(msg: String):
            Callback function that logs the data received from the 'robot_news' topic.

    Usage:
        Instantiate this class within a ROS2 Python node to listen for and log robot news updates.
    """
    def __init__(self):
        super().__init__("smartphone")
        self.suscriber = self.create_subscription(
            String, "robot_news",self.callback_robot_news,10
        )
        self.get_logger().info("smartphone has started")
    def callback_robot_news(self, msg:String):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args) 
    node = SmartphoneNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
