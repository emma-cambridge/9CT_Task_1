#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

ultrasonic_sensor = UltrasonicSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.turn(-10)
robot.turn(-10)
robot.straight(180)
robot.turn(-40)
robot.turn(-42)

robot.straight(500)

#if ultrasonic_sensor.distance() > 200:
    #ev3.speaker.beep




#ev3.speaker.beep()

#robot.turn(-110)
#ev3.speaker.beep()

#robot.straight(300)
#ev3.speaker.beep()


#robot.straight(230)

#robot.turn(-50)
#robot.turn(-50)

#robot.straight(395)

#robot.turn(-45)
#robot.turn(-45)
#robot.turn(-20)

#robot.straight(550)

#robot.turn(-110)

#robot.straight(90)