#!/usr/bin/env python

import rospy
import actionlib
from basics_exam.msg import record_odomAction, record_odomResult
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose

class RecordOdomServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('/rec_odom_as', record_odomAction, self.execute, False)
        self.server.start()
        self.positions = []

        self.odom_subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)

    def odom_callback(self, odom_msg):
        # Callback function to receive odometry data
        # Extract position data from the received message
        pose = odom_msg.pose.pose
        position = pose.position
        self.positions.append(position)

    def execute(self, goal):
        # Your logic to record odometry positions every second
        rate = rospy.Rate(1)  # Record positions every second
        for _ in range(60):  # Record for 60 seconds
            rate.sleep()

        # Prepare the result message with recorded positions
        result = record_odomResult(positions=self.positions)
        self.server.set_succeeded(result)

def main():
    rospy.init_node('rec_odom_server')
    server = RecordOdomServer()
    rospy.spin()

if __name__ == '__main__':
    main()
