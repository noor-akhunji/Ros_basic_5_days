#!/usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import LaserScan

class CrashDirectionServer:
    def __init__(self):
        self.direction = "front"  # Default direction
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.service = rospy.Service('/crash_direction_service', Trigger, self.handle_crash_direction)

    def laser_callback(self, data):
        # Process laser scan data to determine direction
        # For example, you can check the minimum distance on the sides to detect obstacles
        # Update self.direction accordingly
        pass

    def handle_crash_direction(self, req):
        # Return the determined direction
        return TriggerResponse(success=True, message=self.direction)

def main():
    rospy.init_node('crash_direction_server')
    server = CrashDirectionServer()
    rospy.spin()

if __name__ == "__main__":
    main()
