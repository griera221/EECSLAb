#!/usr/bin/env python
import rospy

from std_msgs.msg import String

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
import sys
def talker():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # std_msgs/String to the topic /chatter_talk
    pub = rospy.Publisher(sys.argv[1]+ '/cmd_vel', Twist, queue_size=10)
    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    r = rospy.Rate(10) # 10hz

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)
        print('enter wasd')
        input_val = input()
        message_sent = Twist()
#        message_sent.linear = [0, 0, 0]
#        message_sent.angular = [0, 0, 0]

        if (input_val == 'w'):
            message_sent.linear.x = 2
        if (input_val == 'a'):
            message_sent.angular.z = 1
        if (input_val == 's'):
            message_sent.linear.x = -2
        if (input_val == 'd'):
            message_sent.angular.z = -1

        #message_sent.msg_timestamp = rospy.get_time()
         
        # Publish our string to the 'chatter_talk' topic
        pub.publish(message_sent)
        #print(rospy.get_name() + ": I sent \"%s\"" % pub_string)
        print("Linear:", message_sent.linear, "Angular:", message_sent.angular)
        
        # Use our rate object to sleep until it is time to publish again
        r.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        talker()
    except rospy.ROSInterruptException: pass

