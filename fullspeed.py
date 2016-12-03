#!/usr/bin/python3

# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import SporosRobot
import RPi.GPIO as GPIO

def move(func):
    def function_wrapper(t):
        print('moving {} for {} seconds'.format(func.__name__,t))
        func(t)
        SporosRobot.stop()
        SporosRobot.wait(0.25)
    return function_wrapper


@move
def leftwheel_forward(t):
    '''left forward'''
    GPIO.output(9,1)
    GPIO.output(10,0)
    time.sleep(t)

@move
def rightwheel_forward(t):
    '''right forward '''
    GPIO.output(7,1)
    GPIO.output(8,0)
    time.sleep(t)

@move
def leftwheel_backward(t):
    '''left backward'''
    GPIO.output(9,0)
    GPIO.output(10,1)
    time.sleep(t)

@move
def rightwheel_backward(t):
    '''right backward '''
    GPIO.output(7,0)
    GPIO.output(8,1)
    time.sleep(t)

@move
def right(t):
    GPIO.output(7,1)
    GPIO.output(8,0)
    GPIO.output(9,0)
    GPIO.output(10,1)
    time.sleep(t)

@move
def left(t):
    GPIO.output(7,0)
    GPIO.output(8,1)
    GPIO.output(9,1)
    GPIO.output(10,0)
    time.sleep(t)

@move
def afw(t):
    ''' all forward '''
    GPIO.output(9,1)
    GPIO.output(10,0)
    GPIO.output(7,1)
    GPIO.output(8,0)
    time.sleep(t)

    @move
    def abw(t):
        ''' all backward '''
        GPIO.output(9,0)
        GPIO.output(10,1)
        GPIO.output(7,0)
        GPIO.output(8,1)
        time.sleep(t)

    def astop():
        ''' all stop '''
        for pin in [7,8,9,10]:
            GPIO.output(pin,0)


    def wait(t):
        print('waiting:',t)
        time.sleep(t)

    setup_GPIO()
    cmd = 'go'

    while cmd not in ('','exit'):
        cmd = input('direction, time: ')
        try: d, t = cmd.split(',')
        except: 
            astop()
            print('exiting')
            return
        t = float(t)
        if d is 'f':
            afw(t)
        elif d is 'b':
            abw(t)
        elif d is 'r':
            right(t)
        elif d is 'l':
            left(t)
        else:
            print('enter l,r,b,f,w, or exit')
        astop()
    GPIO.cleanup()

if __name__ == '__main__':
    drive()
