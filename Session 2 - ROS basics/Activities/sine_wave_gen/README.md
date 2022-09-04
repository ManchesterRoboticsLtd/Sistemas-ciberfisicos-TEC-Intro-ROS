# Session 3 Activities

### Requirements
* Puzzlebot Gazebo simulator running (see Session 3)
* Copy the folder open_loop_ctrl into your catkin_ws/src folder, the folder should look as follows
<img src="https://user-images.githubusercontent.com/67285979/187089591-091a9058-dcc1-4abe-80fa-c4405f29bcea.png" alt="drawing" width="400"/>
* Compile the files using catkin_make from terminal

## Example 1
* An example of a basic node to control the simuated puzzlebot can be found in open_loop_ctrl/scripts/straightLine.py
  - the example can be run using the launch command 

```
roslaunch open_loop_ctrl straightLine.launch
```

## Activity 1 
* Drive the Gazebo model of the Puzzlebot in a Straight Line (2 meters)
  - Modify the file straightLine.py (open_loop_ctrl/scripts/straightLine.py) to make the robot move for 2 meters using an open loop controller.
  - Compile your program
  - Use the previously defined launch file to launch all your nodes and gazebo
```
roslaunch open_loop_ctrl straightLine.launch
```
  - Note: You do not need to modify the CMake (unless you need to use a non-standard library)

## Activity 2
* Drive the Gazebo model of the Puzzlebot in a square pth o a side lenght 2 meters.
  - Modify the file square.py (open_loop_ctrl/scripts/square.py) to make the robot move in a suqare using an open loop controller.
  - Compile your program
  - Use the pre-made square.launch to launch all your nodes and gazebo
```
roslaunch open_loop_ctrl square.launch
```
  - Note: You do not need to modify the CMake (unless you need to use a non-standard library)
