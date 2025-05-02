#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase


ev3 = EV3Brick()

obstacle_sensor = UltrasonicSensor(Port.S4)
colour_sensor = ColorSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

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