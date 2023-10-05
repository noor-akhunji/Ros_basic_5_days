#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan #import sensor & leser scan library
from geometry_msgs.msg import Twist

def callback(msg): 
  print(msg.ranges[360]) 

#When distance to an obstacle is infront of the robot is >1 meter then robot move forward
  if msg.ranges[360] > 1.0:
      move.linear.x = 0.1 #move_linear in x direction
      move.angular.z = 0.0 #move_angular in z direction

#When distance to an obstacle infront of the robot is <1 meter then robot turn left
  if msg.ranges[360] < 1.0: 
      move.linear.x = 0.0 #move_linear in x direction
      move.angular.z = 0.2 #move_angular in z direction
        
#When distance to an obstacle at left-side of robot is <0.3 meters, the robot turn right
  if msg.ranges[0] < 1.0:
      move.linear.x = 0.0 #move_linear in x direction
      move.angular.z = -0.2 #move_angular in z direction
        
#When distance to an obstacle at right-side of robot is <0.3 meters, the robot turn left
  if msg.ranges[0] < 1.0:
      move.linear.x = 0.0 #move_linear in x direction
      move.angular.z = 0.2 #move_angular in z direction
      
  pub.publish(move)

rospy.init_node('topics_quiz_node')
 #it will subscribe to the laser scan topic on robot
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()