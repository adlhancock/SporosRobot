#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:15:01 2016

@author: David
"""
from .context import SporosRobot
from SporosRobot import initialise, cleanup

def drive():
    from SporosRobot.fullspeed import forward, backward, left, right, stop
    cmd = 'go'
    
    while cmd not in ('','exit'):
        cmd = input('direction, time: ')
        try: d, t = cmd.split(',')
        except: 
            stop()
            print('exiting')
            return
        t = float(t)
        if d is 'f':
            forward(t)
        elif d is 'b':
            backward(t)
        elif d is 'r':
            right(t)
        elif d is 'l':
            left(t)
        else:
            print('enter l,r,b,f,w, or exit')
        stop()

if __name__ == '__main__':
    initialise()
    drive()
    cleanup()
