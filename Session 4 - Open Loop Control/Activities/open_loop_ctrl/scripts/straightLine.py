#!/usr/bin/env python
import rospy
# Library that contains standard and geometry ROS msgs
from geometry_msgs.msg import Twist

class open_loop_ctrl:
	def __init__(self):
		#Set the time to move the robot in a straight line
		self.time=10
		# Setup Variables to be used
		self.first = True
		self.start_time=0.0
		self.current_time=0.0


		#Setup Control Message to be used
		self.control = Twist()
		self.control.linear.x = 0.0
		self.control.linear.y = 0.0
		self.control.linear.z = 0.0
		self.control.angular.x = 0.0
		self.control.angular.y = 0.0
		self.control.angular.z = 0.0

		#Setup ROS publishers
		self.vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    	
	def run(self):
		#Run this code only at the beginning
		if (self.first):
			#Wait for the first time to be published from gazebo
			while not rospy.get_time():
				pass
			#Initialise variables to use the first iteration before entering the loop
			self.current_time=rospy.get_time()
			self.start_time=rospy.get_time()
			self.first=False
            
		else:
			#Calculate time
			self.current_time=rospy.get_time()
			dt=self.current_time-self.start_time
			#If the time is greater than the established time to go straight stop the robot
			if (dt>self.time):
				self.stop()

			else:
				#Set the desired linear and angular speeds of the robot
				self.control.linear.x= 0.8
				self.control.angular.z = 0.0
	
				#Publish the control inputs
				self.vel_pub.publish(self.control)
        	    
	
    #Stop Condition
	def stop(self):
		#Setup the stop message (can be the same as the control message)
		print("Stopping")
		msg = Twist()
		msg.linear.x = 0
		msg.linear.y = 0
		msg.linear.z = 0
		msg.angular.x = 0
		msg.angular.y = 0
		msg.angular.z = 0
		self.vel_pub.publish(msg)

if __name__ == '__main__':
    #Initialise and Setup node
	rospy.init_node("Move_Straight")
	RobotCtrl = open_loop_ctrl()
	loop_rate = rospy.Rate(10)
	rospy.on_shutdown(RobotCtrl.stop)

    #Run node
	print("Run")    
	try:
		while not rospy.is_shutdown():
			RobotCtrl.run()
			loop_rate.sleep()

	except rospy.ROSInterruptException:
		pass
