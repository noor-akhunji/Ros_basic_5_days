#!/usr/bin/env python

import rospy
import actionlib
from std_srvs.srv import Trigger
from basics_exam.msg import record_odomAction, record_odomGoal
from geometry_msgs.msg import Twist


def move_robot(direction):
    # Create a Twist message to control the robot's movement
    cmd_vel = Twist()

    # Set default velocities (stop the robot)
    linear_velocity = 0.0
    angular_velocity = 0.0

    # Set velocities based on the specified direction
    if direction == "front":
        linear_velocity = 0.2  # Move forward with a linear velocity of 0.2 m/s
    elif direction == "left":
        angular_velocity = 0.5  # Turn left with an angular velocity of 0.5 rad/s
    elif direction == "right":
        angular_velocity = -0.5  # Turn right with an angular velocity of -0.5 rad/s

    # Set the velocities in the Twist message
    cmd_vel.linear.x = linear_velocity
    cmd_vel.angular.z = angular_velocity

    # Publish the Twist message to control the robot's movement
    cmd_vel_pub.publish(cmd_vel)


def main_program():
    rospy.init_node('main_program')

    # Wait for services and action servers to be available
    rospy.wait_for_service('/crash_direction_service')
    crash_direction_service = rospy.ServiceProxy('/crash_direction_service', Trigger)

    client = actionlib.SimpleActionClient('/rec_odom_as', record_odomAction)
    client.wait_for_server()

    # Create a goal instance and send it to the action server
    goal = record_odomGoal()  # Create an instance of record_odomGoal
    client.send_goal(goal)  # Send the goal to the action server

    # Logic to move the robot and get direction from the service
    while not rospy.is_shutdown():
        direction_response = crash_direction_service()
        direction = direction_response.message

        # Move the robot in the specified direction
        move_robot(direction)

        # Check if 60 seconds have passed or if the robot has exited the room
        if client.wait_for_result(rospy.Duration.from_sec(60.0)) or direction == "exit":
            break

    # Stop the robot before exiting
    move_robot("stop")

    print("Robot has exited the room.")

if __name__ == '__main__':
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)  # Publisher for controlling robot movement
    main_program()

