#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty

rospy.init_node('bb8_move_in_circle_service_client')
rospy.wait_for_service('/move_bb8_in_circle')

try:
    move_bb8_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
    response = move_bb8_service()
    rospy.loginfo("BB-8 movement service call successful!")
except rospy.ServiceException as e:
    rospy.logerr("Service call failed: %s" % e)
