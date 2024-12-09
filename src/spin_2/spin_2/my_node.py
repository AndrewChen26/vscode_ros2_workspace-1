import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist




class SpinNode(Node):
    def __init__(self):
        super().__init__('spin_node')


        # Create publisher, set the message type, and the topic to publish
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)


        # Timer to activate callback function every "timer_period" seconds
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.velocity_callback)


    def velocity_callback(self):
        twist = Twist()
        twist.linear.x = 1.0  # Move forward at 1 m/s
        twist.angular.z = 0.5  # Rotate at 0.5 rad/s


        # Publish the twist message
        self.publisher_.publish(twist)
        self.get_logger().info(
            'Publishing: Linear x: %.2f, Angular z: %.2f' % (twist.linear.x, twist.angular.z)
        )




def main(args=None):
    rclpy.init(args=args)


    spin_node = SpinNode()


    rclpy.spin(spin_node)


    # Destroy the node explicitly (optional)
    spin_node.destroy_node()
    rclpy.shutdown()




if __name__ == '__main__':
    main()