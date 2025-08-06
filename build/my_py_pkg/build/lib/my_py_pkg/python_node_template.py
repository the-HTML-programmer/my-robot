#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyCustomNode(Node):   #modifyname
    def __init__(self):
        super().__init__("node_name") #modifyname


def main(args=None):
    rclpy.init(args=args) 
    node = MyCustomNode()  #modifyname
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
