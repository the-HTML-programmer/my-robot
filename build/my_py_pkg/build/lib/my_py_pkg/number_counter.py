#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):  
    def __init__(self):
        super().__init__("number_counter") 
        self.counter = 0
        self.number_counter_publisher = self.create_publisher(Int64,"number_count",10)
        self.number_counter_subcriber =self.create_subscription(
            Int64,"number",self.callback_number_counter,10)
        self.number_counter_service = self.create_service(SetBool,"reset_counter",self.callback_number_counter_service)

        self.get_logger().info("number counter has been started")


    def callback_number_counter(self,msg:Int64):
        self.counter += msg.data 
        new_msg = Int64()
        new_msg.data = self.counter
        self.number_counter_publisher.publish(new_msg)

    def callback_number_counter_service(self,request:SetBool.Request,response:SetBool.Response):
        if request.data:
            self.counter = 0
            response.success = True 
            response.message = "Counter reset to 0"
        
        else:
            response.success = False
            response.message = "Counter reset FAILED"
        return response


        
 
def main(args=None):
    rclpy.init(args=args) 
    node = NumberCounterNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__" :
    main()
