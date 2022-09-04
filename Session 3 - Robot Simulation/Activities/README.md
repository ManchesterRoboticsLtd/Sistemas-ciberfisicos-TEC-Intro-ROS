# Session 3 Activities

### Requirements
* Puzzlebot Gazebo simulator running (see Session 3 presentation)


## Activity 1
* Add files to your catkin workspace, and compile them. The workspace whould look like the following image (without the **open_loop_ctrl** folder)
<img src="https://user-images.githubusercontent.com/67285979/187089591-091a9058-dcc1-4abe-80fa-c4405f29bcea.png" alt="drawing" width="400"/>
* Use the launch file to launch your robot:

```
roslaunch puzzlebot_world puzzlebot_tec_simple_world.launch
```

## Activity 2
*Install the teleop package using:
```
sudo apt get install ros noetic teleop twist keyboard
```
* Run

```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
* Input in the terminal the commands to move the robot (use the keyboard as explained in the terminal instructions)
* See how the robot traverses accordingly the environment.

## Activity 3

* Open Gazebo using the command in the terminal:
```
gazebo
```
* Using the interface, create a world with the information described in Diagram 1.
* Save the world with the name “custom_room1.world”.
* Use the following command to spawn the puzzle in the world you saved.
```
roslaunch puzzlebot_world puzzlebot_tec_simple_world_edited.launch
```
<img src="https://user-images.githubusercontent.com/67285979/188334571-11f75f8a-f267-4cb7-8c93-180c75d6171d.png" alt="Diagram 1" width="400"/>

