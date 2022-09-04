# Session 5 Activities

### Requirements
* Puzzlebot Gazebo simulator running (see Session 3)
* Copy the folder close_loop_ctrl into your catkin_ws/src folder, the folder should look as follows
<img src="https://user-images.githubusercontent.com/67285979/188336210-f823a50f-e26a-4968-9777-14740d895318.png" alt="drawing" width="400"/>

* Compile the files using *catkin_make* from terminal

## Example 1
* An example of a basic node to subscribe and publish data to the the PuzzleBot Gazebo Simulation can be found in close_loop_ctrl/scripts/straightLine.py
  - the example can be run using the launch command 

```
roslaunch close_loop_ctrl straightLine.launch
```
* The velocity published into the */wr* topic will be displayed on the terminal
<img src="https://user-images.githubusercontent.com/67285979/188336351-a936ad23-3c06-49b4-8c48-db160e41874d.png" alt="drawing" width="400"/>

* Alternatively, you can use *rqt_graph* to verify if the node is subscribed to the /wr topic   

## Activity 1 
* Implement a ROS node that computes the robot location using the information from the gazebo simulator (Gazebo Simulator Session 4).
* It should subscribe to /wl and /wr, and publish the data to a suitable set of topics
* The published messages could be a set floats, or you can combine them in any way you see fit

* You can add your script to the close_loop_ctrl package or make your own package using 
```
catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
```
* Use the teleop package to verify if your results are correct (session 3)
```
sudo apt get install ros noetic teleop twist keyboard
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
  - Note: You do not need to modify the CMake (unless you need to use a non-standard library)

## Activity 2
* Modify the previous node to publish $e_d$ and $e_\theta$. 
* Set a target, and drive the robot around, checking that the angle to the target and the distance from the target are updated correctly
* Remember to wrap all angles to within 1 circle (wrap to pi or wrap to 2 pi)

* Use the teleop package to verify if your results are correct (session 3)
```
sudo apt get install ros noetic teleop twist keyboard
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
  - Note: You do not need to modify the CMake (unless you need to use a non-standard library)
  
## Activity 3
* Move te robot (Gazebo Simulator Session 4) from an initial position to a final position using a Proportional Control (P-Control)
<img src="https://user-images.githubusercontent.com/67285979/188335003-d01d67bd-c9a8-4fbb-b0f4-7acb7c05d4f3.png" alt="drawing" width="400"/>

