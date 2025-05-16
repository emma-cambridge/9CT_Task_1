# 9CT Assessment Task
By Emma Cambridge  
# Requirements Outline
I need to create a program for my EV3 robot that allows it to move two blocks to the start zone and dodge two other blocks using two sensors. The program will need to:
- Object Detection: The robot must stop when an object is detected within 10cm
    - Use Case: The robot is navigating and encounters an object. The ultrasonic sensor detects the object within 10cm. The robot stops moving forward. The robot stops 10cm away from the object.
- Check Colour: The robot must use the colour sensor to check whether the object is blue or green, or red or yellow.
    - Use Case: An object is detected in front of the robot. The colour sensor checks whether the colour is blue or green, or red or yellow. The object is detected as red. The robot begins the capturing process.
- Capture the Object: If the colour is detected as yellow or red then the robot must use a skewer attachment to grab the object.
    - Use Case: The colour of an object 10cm in front of the robot is detected as yellow. (No inputs). The robot moves forward to skewer the middle of the object. The object has a skewer through it.
- Drag the Object: After capturing the object the robot must turn 180 degrees and return to the start zone.
    - Use Case: An object in front of the robot has been captured by the skewer attachment. (No inputs). The robot turns 180 degrees and drags the object with it into the start zone. The object and robot are in the start zone area.

## Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
| Detects Obstacle  |  Ultrasonic sensor detects <10cm   |   The robot stops moving forward   |
|  Checks Colour  | Detects colour as blue, green, yellow, or red |  The robot returns the colour and will initiate capture/turn and move away  |
| Captures Object  |  NONE  |  The object has a skewer through it |
| Drags Object | NONE | The object is within the start zone | 

## Non-Functional Requirements
As well as completing the above requirements the robot should react to the ultrasonic sensor's inputs within 2 seconds to prevent it from crashing into an object, complete the task with a moderate level of efficiency (it shouldn't take hours to get the blocks), and accurately skewer the blocks and drag them back to the starting area. 


# Design
~~~
BEGIN
    drive forward
    object_detection
    colour_check
    object_capture
    object_drag 
END
~~~
![Mainline Routine Flowchart](mainline_routine.png "Mainline Routine")
~~~
BEGIN colour_check
    INPUT colour sensor
    IF colour sensor = red or yellow THEN
        initiate object_capture
    ELSE
        turn 90 degrees
    ENDIF
END
~~~
![Colour Check Flowchart](colour_check.png "Colour Check")
~~~
BEGIN object_detection
    WHILE distance > 100mm
        INPUT distance
        Drive forward
    ENDWHILE
        Stop
END
~~~

![Object Detection Flowchart](object_det.png "Object Detection")

# Test Cases
## Outline
I want to create a program that will sense the colour of the block. It'll input the colour then decide if it is yellow, red, green, or blue. If it's blue or green it'll turn and if it's anything else it'll continue to capturing the object.

## Testing
I managed to get the colour sensing after some trial and error where I realised that I needed to add this line to the top of my code
~~~
from pybricks.parameters import Port, Color
~~~
so that the robot would understand what colour is. After that I managed to get the robot moving and the robot to stop when it sensed a green or blue block, with this code:
~~~
robot.drive(100, 0)

while True:

    while obstacle_sensor.distance() > 100:
        robot.drive(100, 0)

    if colour_sensor.color() == Color.GREEN:
        stop()
    elif colour_sensor.color() == Color.BLUE:
        stop()
    else:
        ev3.speaker.beep()
~~~
However, after some testing I decided that I didn't actually want to implement a colour sensing function because the robot would skip through the if statement if it sensed any other colour, including the grey on the blocks. Overall I decided that the design was too fidley and had too much room for error, and decided to use the colour sensor to make sure the robot doesn't go off the line instead.

# Evaluation
## Evelyn
- 4/5 for effort: Evelyn helped with some of the coding and helped a lot with testing and debugging.
- 3/5 for contribution: Evelyn helped me quite a bit with the testing but didn't do as much with the original code.
- 5/5 for final test case: We all shared a final test case so I guess it was good??
- 5/5 performance: Evelyn was super encouraging and I think she did everything we asked of her to her best ability throughout the project
## Juliet
- 4/5 for effort: Juliet was always really passionate about what she was doing and I think she really tried her best
- 5/5 for contribution: Juliet was really good at coming up with ideas and her touch sensor idea was really helpful in getting enough sensors into the final project. She also made the weird stag beetle thing that picked up the blocks so we definitely couldn't have done the project without her
- 5/5 for test case: Same as Evelyn
- 4/5 for performance: Juliet's weird stag beetle thing was a little bit fragile but given the amount she contributed I think it's very fair to say that she had a really good performance throughout the project.

## Final Evaluation Questions
I don't think I did a great job at fulfilling the requirements outline, if I'm being honest. After the first round of testing I realised that the requirements I had set out were unreasonable and that I wouldn't be able to code a working program within the time limit if I followed this outline so I pivoted completely and hardcoded the entire program, so while I didn't 