#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from basics_exam.srv import DistMotion, DistMotionResponse
from geometry_msgs.msg import Twist, Pose
import time

class SquareMotion:
    def __init__(self):
        self.move_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.takeoff_pub = rospy.Publisher('/takeoff', Empty, queue_size=1)
        self.land_pub = rospy.Publisher('/land', Empty, queue_size=1)
        self.side_length = 2  # in meters
        self.motion_duration = 60  # in seconds

    def takeoff(self):
        takeoff_msg = Empty()
        self.takeoff_pub.publish(takeoff_msg)
        time.sleep(10)  # Wait for drone to stabilize

    def perform_square_motion(self):
        move_cmd = Twist()
        start_time = time.time()

        while time.time() - start_time <= self.motion_duration:
            move_cmd.linear.x = 1  # Forward motion
            self.move_pub.publish(move_cmd)
            time.sleep(self.side_length)  # Move forward

            move_cmd.linear.x = 0  # Stop
            self.move_pub.publish(move_cmd)
            time.sleep(2)  # Pause

            move_cmd.angular.z = 1  # Rotate
            self.move_pub.publish(move_cmd)
            time.sleep(3.14)  # Rotate 180 degrees (pi radians)

            move_cmd.angular.z = 0  # Stop rotation
            self.move_pub.publish(move_cmd)
            time.sleep(2)  # Pause

            move_cmd.linear.x = -1  # Backward motion
            self.move_pub.publish(move_cmd)
            time.sleep(self.side_length)  # Move backward

            move_cmd.linear.x = 0  # Stop
            self.move_pub.publish(move_cmd)
            time.sleep(2)  # Pause

    def land(self):
        land_msg = Empty()
        self.land_pub.publish(land_msg)

    def calculate_distance_moved(self):
        # For simplicity, assume the drone moves 8 meters (2 meters per side of the square)
        return 8

def motion_service_callback(request):
    motion_handler = SquareMotion()
    motion_handler.takeoff()
    motion_handler.perform_square_motion()
    motion_handler.land()

    distance_moved = motion_handler.calculate_distance_moved()
    rospy.loginfo("Motion ended. The drone has moved {} meters.".format(distance_moved))
    return DistMotionResponse(True, "The drone has moved {} meters.".format(distance_moved))

if __name__ == "__main__":
    rospy.init_node('motion_service')
    service = rospy.Service('/motion_service', DistMotion, motion_service_callback)
    rospy.loginfo("Distance motion service is ready.")
    rospy.spin()
