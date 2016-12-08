#! /usr/bin/python3
"""

"""

all = ['initialise',
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

import fullspeed

from SporosRobot.system import initialise, cleanup

# from fullspeed import left, right, forward, backward, stop


