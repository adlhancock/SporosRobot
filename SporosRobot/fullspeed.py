#!/usr/bin/python3

"""
fullspeed.py

CamJam EduKit 3 - Robotics

"""


def move(func):
    def function_wrapper(t):
        from RPi.GPIO import output as setpin
        print('moving {} for {} seconds'.format(func.__name__,t))
        func(t)
        stop()
    return function_wrapper

@move
def right(t):
    setpin(7,1)
    setpin(8,0)
    setpin(9,0)
    setpin(10,1)
    wait(t)

@move
def left(t):
    setpin(7,0)
    setpin(8,1)
    setpin(9,1)
    setpin(10,0)
    wait(t)

@move
def forward(t):
    ''' all forward '''
    setpin(9,1)
    setpin(10,0)
    setpin(7,1)
    setpin(8,0)
    wait(t)

@move
def backward(t):
    ''' all backward '''
    setpin(9,0)
    setpin(10,1)
    setpin(7,0)
    setpin(8,1)
    wait(t)

def stop():
    ''' all stop '''
    for pin in [7,8,9,10]:
        setpin(pin,0)

"""
@move
def leftwheel_forward(t):
    '''left forward'''
    setpin(9,1)
    setpin(10,0)
    time.sleep(t)

@move
def rightwheel_forward(t):
    '''right forward '''
    setpin(7,1)
    setpin(8,0)
    time.sleep(t)

@move
def leftwheel_backward(t):
    '''left backward'''
    setpin(9,0)
    setpin(10,1)
    time.sleep(t)

@move
def rightwheel_backward(t):
    '''right backward '''
    setpin(7,0)
    setpin(8,1)
    time.sleep(t)

"""
