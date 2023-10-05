import rospy
import actionlib
from basics_exam.msg import RecordPoseAction, RecordPoseResult
from nav_msgs.msg import Odometry

class RecordPoseServer:
    def __init__(self):
        self._as = actionlib.SimpleActionServer('/rec_pose_as', RecordPoseAction, self.execute, False)
        self._as.start()
        self.poses = []

    def execute(self, goal):
        rate = rospy.Rate(1)  # Record poses every second for 20 seconds
        for _ in range(20):
            # Get the drone's position from Odometry and append to the list
            # odom = ...  # Get the Odometry data
            # pose = odom.pose.pose
            # self.poses.append(pose)
            # For demonstration purposes, assuming a constant position
            pose = Odometry().pose.pose
            self.poses.append(pose)
            rate.sleep()

        result = RecordPoseResult()
        result.poses = self.poses
        self._as.set_succeeded(result)

rospy.init_node('check_distance_action')
server = RecordPoseServer()
rospy.spin()
