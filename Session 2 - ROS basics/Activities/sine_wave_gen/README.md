# Session 2 Activities

### Requirements
* Ubuntu in VM or dual booting
* ROS installed
* Copy the folder sine_wave_gen into your catkin_ws/src folder
* Compile the files using catkin_make from terminal (fromthe catkin_ws folder)

## Activity 1 
* Create your package called basic_comms ””(the dependencies used are rospy and std_msg
* Implement the code in Python ..(This must be placed in the src folder of your package)
* Modify your Cmakelist txt and the package xml file to include your code You can find help [here](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
* Use some of the command tools to verify the correct functioning of the system Hint Go back to slides about the talker and the listener
* Use the following commands in different terminals to run and test your nodes independently.
```
roscore
rosrun basic_comms talker.py
rostopic echo /chatter
```
```
roscore
rosrun basic_comms listener.py
rostopic pub /chatter <tab complete>
```

  - Note: You do not need to modify the CMake (unless you need to use a non-standard library)
  - Remember to make the nodes executable using the the following command inside the catkin_ws/src/basic_comms/src and catkin_ws/src/basic_comms/src
 folders 
```
 chmod +x talker.py
 chmod +x listener.py
```

## Activity 2
* Use the node template “sine_wave.py” to code the node in Python. You must use a custom message
for the signal.
* Edit the message file in the msg folder of your template
* Launch both the sine wave node and rqt . Use the following command:
```
roslaunch sine_wave_gen sine_wave_gen.launch
```
  - Note: You do not need to modify the CMake (unless you need to use a non-standard library)
  - Remember to make the node executable using the the following command inside the catkin_ws/src/sine_wave_gen/src
 folder 
```
 chmod +x sine_wave.py 
```
