#!/usr/bin/env python

import rospy
import actionlib
from drone_square_move.action import TestAction, TestGoal

rospy.init_node('drone_square_client')
client = actionlib.SimpleActionClient('drone_square', TestAction)
client.wait_for_server()

goal = TestGoal()
goal.side_length = 5  # Specify the side length of the square

client.send_goal(goal)

client.wait_for_result()
print("Result:", client.get_result())
