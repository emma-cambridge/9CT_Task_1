#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.straight(180)
ev3.speaker.beep()

robot.turn(-110)
ev3.speaker.beep()

robot.straight(300)
ev3.speaker.beep()

#grabby grabby process here

robot.straight(230) # small amount

robot.turn(-45) # eensie weensie bit
robot.turn(-45)

#grabby grabby

robot.straight(395)

robot.turn(-45)
robot.turn(-45)
robot.turn(-20)

robot.straight(550)

robot.turn(-110)

robot.straight(100)