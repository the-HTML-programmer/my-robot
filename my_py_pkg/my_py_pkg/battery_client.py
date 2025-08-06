#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedState

class BatteryClientNode(Node):  
    def __init__(self):
        super().__init__("battery_client") 
        self.battery_client = self.create_client( LedState,"set_led")

    def call_battery_client(self,a,b):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("waiting for LED panel server...")
        request = LedState.Request()
        request.a = a
        request.b = b


def main(args=None):
    rclpy.init(args=args) 
    node = BatteryClientNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
