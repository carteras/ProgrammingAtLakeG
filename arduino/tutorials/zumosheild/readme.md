# Using the Zumo

## imports
To use the ZumoShield, you need to import the appropriate libraries. 

The specific library that we need is ZumoShield.h

All of the example code includes Wire.h, so I have included it here.
```cpp
#include <Wire.h>
#include <ZumoShield.h>
```

## global variables 
To use the various components of the ZumoShield, we need to have some global variables set up for us. This includes the ZumoBuzzer (to play music), the ReflectanceSensorArray (to read the line), the motors (to drive), and the button to handle some interactions. 

These sit in the global space outside of functions. 

```cpp
ZumoBuzzer buzzer;
ZumoReflectanceSensorArray reflectanceSensors;
ZumoMotors motors;
Pushbutton button(ZUMO_BUTTON);
```


## Thinking in states
We have broadly talked about state, both in the lecture on state but also in the video release that works with this document.

Here, we are doing two things. The first is we are going to define all of the possible types of state a robot can be in. Broadly speaking, we have at least 3 states: 
LINE_TRACKING
OBJECT_AVOIDANCE
LINE_FINDING

We assign these to numbers and use the label for our reference. Remember not to double up, so you have two states with the same number. 

We also capture the state that the robot is currently in. We want to initialise this state to the default starting state. 

You could argue that the default starting state could be CALIBRATE.  

 
```cpp
//define all of the states that your robot can 
//be in
int LINE_TRACKING = 1;
int OBJECT_AVOIDANCE = 2;
int LINE_FINDING = 3;

//set the state to default on your desired 
//starting state
int STATE = LINE_FINDING; 
```

## button pushing
```cpp
button.waitForButton();
```

## Calibrating the reflective sensors
```cpp
int i;
  for (i = 0; i < 80; i++)
  {
    if ((i > 10 && i <= 30) || (i > 50 && i <= 70))
      motors.setSpeeds(-200, 200);
    else
      motors.setSpeeds(200, -200);
    reflectanceSensors.calibrate();

    // Since our counter runs to 80, the total delay will be
    // 80*20 = 1600 ms.
    delay(20);

  }
  motors.setSpeeds(0, 0);
```
## moving the zumo
```cpp
//forward
motors.setSpeed(400,400);

//turn left
motors.setSpeed(0, 400);

//turn right
motors.setSpeed(400, 0);

//backard
motors.setSpeed(-400, -400);

//mad doughnuts
motors.setSpeed(-400, 400);
```

## Line Sensor
```cpp
int lineSensor(){
    unsigned int sensors[6];
    int pos = reflectanceSensors.readLine(sensors);
    int error = pos - 2500;
    return error;
}
```
