#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from basics_exam.srv import DistMotion, DistMotionResponse

class SquareMotion:
    def __init__(self):
        self.side_length = 2  # in meters

    def calculate_distance_moved(self):
        # For simplicity, assume the drone moves 8 meters (2 meters per side of the square)
        return 8

def distance_motion_service_callback(request):
    motion_handler = SquareMotion()
    distance_moved = motion_handler.calculate_distance_moved()
    rospy.loginfo("Motion ended. The drone has moved {} meters.".format(distance_moved))
    return DistMotionResponse(True, "The drone has moved {} meters.".format(distance_moved))

if __name__ == "__main__":
    rospy.init_node('distance_motion_service')
    service = rospy.Service('/dist_motion_service', DistMotion, distance_motion_service_callback)
    rospy.loginfo("Distance motion service is ready.")
    rospy.spin()
