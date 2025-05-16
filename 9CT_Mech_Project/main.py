#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.ev3devices import TouchSensor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

ultrasonic_sensor = UltrasonicSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

touch_sensor = TouchSensor(Port.S2)

while True:
    if touch_sensor.pressed():
        ev3.speaker.beep()

        robot.turn(-10)
        robot.turn(-10)
        robot.straight(180)
        robot.turn(-40)
        robot.turn(-42)

        robot.straight(500)

        if ultrasonic_sensor.distance() > 200:
            ev3.speaker.beep

        robot.turn(-50)
        robot.turn(-50)

        robot.straight(440)

        robot.turn(-45)
        robot.turn(-45)
        robot.turn(-20)

        robot.straight(520)

        robot.turn(-100)
        robot.straight(40)