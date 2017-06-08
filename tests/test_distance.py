#! /usr/bin/python3

""" quick script for running SporosRobot

"""

import os
import sys

sys.path.append('/home/pi/python/SporosRobot/')

import SporosRobot

SporosRobot.distance()
setup_ears()
get_distance()
