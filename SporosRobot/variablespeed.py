#!/usr/bin/python3

"""
testing pulse width modulation to get variable speed for sporos robot

"""

import RPi.GPIO as GPIO 
from time import sleep as wait

#assign pins

from SporosRobot.system import lfw,lbw,rfw,rbw,motor_pins,setup_GPIO,setup_pwm

setup_GPIO()
pwm = setup_pwm()


def directions(pwm):
    """
    returns: 
        left, right, forward, backward, stop
    """
            
    def set_speed(pwm,pin,duty):
            pwm[pin].ChangeDutyCycle(duty)
    
    def move(func):
        def function_wrapper(speed,t):
            assert 0<=speed<=100, 'speed must be between 0 and 100'
            print('moving {} at {}% for {} seconds'.format(func.__name__,speed,t))
            func(speed)
            wait(t)
            stop()
        return function_wrapper
    
    @move
    def right(speed):
        '''rotate right'''
        set_speed(rfw,speed)
        set_speed(lfw,0)
        set_speed(rbw,0)
        set_speed(lbw,speed)
    
    @move
    def left(speed):
        '''rotate left'''
        set_speed(rfw,0)
        set_speed(lfw,speed)
        set_speed(rbw,speed)
        set_speed(lbw,0)
    
    @move
    def forward(speed):
        ''' all forward '''
        set_speed(rfw,speed)
        set_speed(lfw,speed)
        set_speed(rbw,0)
        set_speed(lbw,0)
    
    @move
    def backward(speed):
        ''' all backward '''
        set_speed(rfw,0)
        set_speed(lfw,0)
        set_speed(rbw,speed)
        set_speed(lbw,speed)
    
    def stop():
        ''' all stop '''
        for pin in motor_pins:
            set_speed(pin,0)
            
    def go():
        direction = {'f':forward,
                     'b':backward,
                     'l':left,
                     'r':right}
        cmd = 'go'
        while cmd is not '':
            cmd_string = input('direction+time: ')
            try: 
                commands = cmd_string.split(' ')
                for i in commands:
                    d = i[0]
                    t = float(i[1:])
                    direction[d](speed, t)
            except:
                print('exiting')
                ''' tidy up '''
                stop()
            
    return left, right, forward, backward, stop, go

if __name__ == '__main__':
    setup_GPIO()
    pwm = setup_pwm()
    speed = int(input('speed: '))
    l,r,f,b,stop,go = directions(pwm)
    go()
    GPIO.cleanup()
