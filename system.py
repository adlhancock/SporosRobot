#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Setup for Raspberry Pi Camjam EduKit Robotics hat

Created: 2016-12-03

"""
from RPi.GPIO import cleanup

def initialise():
    import RPi.GPIO as GPIO
    from time import sleep
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    rightforward, rightback, leftforward, leftback = 7,8,9,10
    
    motorpins = [rightforward, rightback, leftforward, leftback]
    
    for pin in motorpins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)
    print('right:{},{} left:{},{}'.format(rightforward,
                                          rightback, 
                                          leftforward, 
                                          leftback))
    return motorpins