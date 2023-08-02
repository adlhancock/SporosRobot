#! /usr/bin/python3

""" quick script for running SporosRobot

"""

import os
import sys

sys.path.insert(0,os.path.abspath('..'))

import SporosRobot

s = SporosRobot.variablespeed()

s.go()
s.stop()
