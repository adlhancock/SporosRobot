#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Full speed test

Created on Sat Dec  3 21:15:01 2016

@author: David
"""

from .context import SporosRobot

def drive():
	s = SporosRobot.fullspeed()
	cmd = "go"
	while True:
		try:
			dirs = {'f':s.forward,'b':s.backward,'l':s.left,'r':s.right}
			cmd = input("[direction], [time]")
			try: 
				d,t = cmd.split(',')
				dirs[d](t)
			except: print("not a command")
		except KeyboardInterrupt:
			print("exiting")
			s.stop()

if __name__ == '__main__':
    drive()