#! /usr/bin/python3
""" SporosRobot: a set of tools for controlling a two wheeled raspberry pi robot

"""

__all__ =     ['variablespeed',
               'fullspeed',
               'setup'
               ]
       
#from time import sleep as wait
#import RPi.GPIO as GPIO
#from RPi.GPIO import cleanup


from .system import setup
from .variablespeed import variablespeed
from .fullspeed import fullspeed


