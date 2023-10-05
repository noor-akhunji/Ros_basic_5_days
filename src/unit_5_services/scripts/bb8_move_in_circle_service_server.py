#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

def move_bb8(req):
    rospy.loginfo("Moving BB-8 in a circle!")
    twist = Twist()
    twist.linear.x = 0.2  # Linear velocity in the x-axis
    twist.angular.z = 0.5  # Angular velocity in the z-axis (for circular motion)
    for _ in range(10):  # Move for a certain duration (adjust as needed)
        bb8_publisher.publish(twist)
        rate.sleep()
    bb8_publisher.publish(Twist())  # Stop BB-8
    return EmptyResponse()

rospy.init_node('bb8_move_in_circle_service_server')
bb8_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(10)  # 10 Hz

rospy.Service('/move_bb8_in_circle', Empty, move_bb8)
rospy.loginfo("Service server is ready to move BB-8 in a circle.")
rospy.spin()
