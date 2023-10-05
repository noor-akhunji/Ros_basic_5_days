#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
import time

rospy.init_node('square_motion')
move_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
takeoff_pub = rospy.Publisher('/takeoff', Empty, queue_size=1)
land_pub = rospy.Publisher('/land', Empty, queue_size=1)
move_cmd = Twist()

# Take off to 5 meters
rospy.loginfo("Taking off...")
takeoff_msg = Empty()
takeoff_pub.publish(takeoff_msg)
time.sleep(10)  # Wait for drone to stabilize

# Move to 5 meters height (adjust this duration based on your drone's speed)
rospy.loginfo("Moving to 5 meters height...")
move_cmd.linear.z = 0.5  # Adjust the ascent speed as needed
move_pub.publish(move_cmd)
time.sleep(10)  # Wait for the drone to reach the desired height

# Stop vertical movement
move_cmd.linear.z = 0
move_pub.publish(move_cmd)

# Square motion
side_length = 2  # in meters
speed = 0.1  # in m/s (adjust this for desired speed)
motion_duration = 60  # in seconds (adjust this for the total motion time)
start_time = time.time()

while time.time() - start_time <= motion_duration:
    # Move forward (one side of the square)
    move_cmd.linear.x = speed
    move_pub.publish(move_cmd)
    time.sleep(side_length / speed)  # Time = Distance / Speed

    # Stop and rotate 90 degrees (pi/2 radians)
    move_cmd.linear.x = 0
    move_cmd.angular.z = 1
    move_pub.publish(move_cmd)
    time.sleep(1.5708)  # 90 degrees in radians
    move_cmd.angular.z = 0
    move_pub.publish(move_cmd)
    time.sleep(1)  # Pause between movements

# Land
rospy.loginfo("Landing...")
land_msg = Empty()
land_pub.publish(land_msg)
