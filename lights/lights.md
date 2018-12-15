#Lights Python-Arduino


#Intro

These files allow the robot's python code to more easily interact with the
lights on the robot.



#Usage

```
from JoyLights import JoyLights

jl = JoyLights('IP ADDRESS', 0)
##Sends lights data to arduino
jl.update_lights(x,y)
```
