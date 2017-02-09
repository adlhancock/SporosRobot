#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Setup for Raspberry Pi Camjam EduKit Robotics hat

Created: 2016-12-03

"""
#global pin assignment
lfw = 7
lbw = 8
rfw = 9
rbw = 10
motor_pins = [lfw,lbw,rfw,rbw]

def setup_GPIO():
    import RPi.GPIO as GPIO 
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    return
           
def setup_pwm(motor_pins,frequency = 50):
    import RPi.GPIO as GPIO
    pwm = {}
    for pin in motor_pins.values():
        GPIO.setup(pin, GPIO.OUT)
        pwm[pin] = GPIO.PWM(pin, frequency)
        pwm[pin].start(0)
    return pwm

def setup_fullspeed(motor_pins):
    import RPi.GPIO as GPIO
    for pin in motor_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,0)
        print('right:{},{} left:{},{}'.format(rfw,rbw,lfw,lbw))
    return motor_pins
