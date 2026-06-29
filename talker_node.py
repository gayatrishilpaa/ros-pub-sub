import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__("talker_node")
        self.publisher_=self.create_publisher(String, 'topic', 10)
        self.create_timer(0.5, self.timer_callback)
        self.count_=0
    
    def timer_callback(self):
        msg=String()
        msg.data="Hello everyone " + str(self.count_)
        self.publisher_.publish(msg)
        self.count_+=1
        self.get_logger( ).info(" Publishing {}". format(msg.data))

def main(args=None):
    rclpy.init(args=args)
    #define node
    talker_node=TalkerNode()
    #use node
    rclpy.spin(talker_node)
    #kill node
    talker_node.destroy_node()
    rclpy.shutdown()

if __name__== '__main__':
    main()