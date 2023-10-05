#!/usr/bin/env python

import rospy
import actionlib
from drone_square_move.action import TestFeedback, TestResult, TestAction

def square_movement(goal):
    # Implement your square movement logic here
    # For example, assuming the drone can move in X and Y directions:
    side_length = goal.side_length
    feedback = TestFeedback()

    for _ in range(4):  # Assuming the drone needs to move on all four sides of the square
        # Move forward (in Y direction)
        # Implement the logic to move the drone forward by side_length units in the Y direction

        # Publish feedback indicating the current side of the square
        feedback.current_side = _ + 1
        server.publish_feedback(feedback)

        # Turn (in X direction)
        # Implement the logic to turn the drone by 90 degrees (or perform a maneuver to change direction)

    # Calculate the total time taken to complete the square
    total_time = 4  # Assuming each side takes 1 unit of time (adjust according to your system)

    # Prepare the result message
    result = TestResult()
    result.total_time = total_time

    # Set the result of the action
    server.set_succeeded(result)

rospy.init_node('drone_square_server')
server = actionlib.SimpleActionServer('drone_square', TestAction, square_movement, False)
server.start()
rospy.spin()
