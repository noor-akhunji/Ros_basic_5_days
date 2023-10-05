#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty

def takeoff():
    rospy.init_node('drone_takeoff', anonymous=True)  # Initialize the ROS node
    takeoff_pub = rospy.Publisher('/takeoff', Empty, queue_size=10)  # Create a publisher for the /takeoff topic
    rospy.sleep(1)  # Wait for the publisher to initialize

    takeoff_msg = Empty()  # Create an Empty message
    takeoff_pub.publish(takeoff_msg)  # Publish the takeoff message

if __name__ == '__main__':
    try:
        takeoff()  # Call the takeoff function
    except rospy.ROSInterruptException:
        pass  # Continue execution if the ROS node is interrupted