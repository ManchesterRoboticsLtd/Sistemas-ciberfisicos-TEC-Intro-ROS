#!/usr/bin/env python
import rospy
import math
# define the custom message definition 

def sine_wave():
    # define publisher with custom message
    # initiatise node 
    
    # hint initialise the time variable
    
    while not rospy.is_shutdown():
        # As we did in the live example, link the variables 
        # with the custom message data accordingly. 
        # Make the necessary calculations for the node to work.  
        
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        sine_wave()
    except rospy.ROSInterruptException:
        pass
