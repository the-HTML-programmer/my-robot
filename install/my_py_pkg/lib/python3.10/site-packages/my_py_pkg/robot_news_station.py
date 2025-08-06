#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewStationNode(Node):   
    def __init__(self):
        super().__init__("robot_news_station") 
        self.declare_parameter("robot_name", "CP30")
        self.declare_parameter("timer",1.0)
        self.robot_name = self.get_parameter("robot_name").value
        self.timer =self.get_parameter("timer").value



        self.publisher_ = self.create_publisher(String, "robot_news",10)
        self.timer_=self.create_timer(self.timer,self.publish_news)
        self.get_logger().info("robot logger has been started")


    def publish_news(self):
        msg=String()
        msg.data = "hello this is " + self.robot_name+ " from robot news"
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args) 
    node = RobotNewStationNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
