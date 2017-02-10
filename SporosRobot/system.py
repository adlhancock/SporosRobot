#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" Setup tools for SporosRobot


For setting up the Camjam EduKit Robotics hat

Created: 2016-12-03

"""


class setup:
    """ Setup tools"""
    def __init__(self):
        """global pin assignment"""
        self.motor_pins = {'lfw':7,
                           'lbw':8,
                           'rfw':9,
                           'rbw':10}

    def GPIO(self):
        """ initialise pins"""
        import RPi.GPIO as GPIO 
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        return
               
    def pwm(self,frequency = 50):
        """ Setup pulse width modulation
        
        Parameters
        ----------
        frequency: :class:`int`
            refresh rate

        Returns
        -------
        pwm : :class:`dict`
            an object containing all the pins

        """

        import RPi.GPIO as GPIO
        pwm = {}
        for pin in self.motor_pins.values():
            GPIO.setup(pin, GPIO.OUT)
            pwm[pin] = GPIO.PWM(pin, frequency)
            pwm[pin].start(0)
        return pwm, self.motor_pins

    def fullspeed(self):
        """ Simple full power output on all motor pins 
        
        Returns
        -------
        motor_pins : :class:`dict'
            a dictionary of named motor pins
        """
        import RPi.GPIO as GPIO
        for pin in self.motor_pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin,0)
            print('right:{},{} left:{},{}'.format(rfw,rbw,lfw,lbw))
        return self.motor_pins
