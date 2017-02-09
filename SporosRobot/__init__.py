#! /usr/bin/python3
""" SporosRobot: a set of tools for controlling a two wheeled raspberry pi robot

"""

__all__ =     ['initialise',
               'cleanup',
               'fullspeed',
               'right',
               'left',
               'forward',
               'backward',
               'stop',
               'wait']
       
from time import sleep as wait
import RPi.GPIO as GPIO
from RPi.GPIO import cleanup

import .fullspeed

import .variablespeed

from .system import initialise, cleanup

from .fullspeed import left, right, forward, backward, stop


