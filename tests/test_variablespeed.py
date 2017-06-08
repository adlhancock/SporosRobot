#! /usr/bin/python3

""" quick script for running SporosRobot

"""

import os
import sys

sys.path.append('/home/pi/python/SporosRobot/')

import SporosRobot

s = SporosRobot.variablespeed()

s.go()
s.stop()
