#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedState
from my_robot_interfaces.srv import SetLed


class LedPanelNode(Node):  
    def __init__(self):
        super().__init__("led_panel") 
        self.led_state = [0,0,0]
        self.led_state_pub = self.create_publisher(LedState,"led_panel_state",10)
        self.led_timer = self.create_timer(5.0,self.publish_led_state)

        self.get_logger().info("LED panel node has been started")


  
    def publish_led_state(self):
        msg = LedState()
        msg.led_state = self.led_state
        self.led_state_pub.publish(msg)

    def callback_set_led(self, request, response):
        led_number = request.led_number
        state = request.state


def main(args=None):
    rclpy.init(args=args) 
    node = LedPanelNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
