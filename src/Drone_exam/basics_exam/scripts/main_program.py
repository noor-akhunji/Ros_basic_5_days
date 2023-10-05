import rospy
import time
import actionlib
from basics_exam.srv import DistMotion, DistMotionRequest
from basics_exam.msg import RecordPoseAction, RecordPoseGoal

rospy.init_node('main_program')

# Call motion service
rospy.wait_for_service('/motion_service')
motion_service = rospy.ServiceProxy('/motion_service')
motion_service()

# Start action server
client = actionlib.SimpleActionClient('/rec_pose_as', RecordPoseAction)
client.wait_for_server()

# Send goal to action server
goal = RecordPoseGoal()  # No goal required
client.send_goal(goal)

# Wait for the action to finish (maximum 60 seconds)
client.wait_for_result(rospy.Duration(60))

# Get the last pose from the action result
last_pose = client.get_result().poses[-1]

# Print the last pose
print("Last Pose:")
print("position:")
print("  x:", last_pose.position.x)
print("  y:", last_pose.position.y)
print("  z:", last_pose.position.z)
print("orientation:")
print("  x:", last_pose.orientation.x)
print("  y:", last_pose.orientation.y)
print("  z:", last_pose.orientation.z)
print("  w:", last_pose.orientation.w)