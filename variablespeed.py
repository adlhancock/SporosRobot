#!/usr/bin/python3

"""
testing pulse width modukation to get variable speed for sporos robot

"""

import RPi.GPIO as GPIO 
from time import sleep as wait

#assign pins
motor_pins = [7,8,9,10]
lfw_pin = 7
lbw_pin = 8
rfw_pin = 9
rbw_pin = 10

frequency = 50


pwm = {} # this is the global pwm object 

def setup_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # pwm = {}
    for pin in motor_pins:
        GPIO.setup(pin, GPIO.OUT)
        pwm[pin] = GPIO.PWM(pin, frequency)
        pwm[pin].start(0)


def set_speed(pin, duty):
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
    set_speed(rfw_pin,speed)
    set_speed(lfw_pin,0)
    set_speed(rbw_pin,0)
    set_speed(lbw_pin,speed)

@move
def left(speed):
    '''rotate left'''
    set_speed(rfw_pin,0)
    set_speed(lfw_pin,speed)
    set_speed(rbw_pin,speed)
    set_speed(lbw_pin,0)

@move
def forward(speed):
    ''' all forward '''
    set_speed(rfw_pin,speed)
    set_speed(lfw_pin,speed)
    set_speed(rbw_pin,0)
    set_speed(lbw_pin,0)

@move
def backward(speed):
    ''' all backward '''
    set_speed(rfw_pin,0)
    set_speed(lfw_pin,0)
    set_speed(rbw_pin,speed)
    set_speed(lbw_pin,speed)

def stop():
    ''' all stop '''
    for pin in motor_pins:
        set_speed(pin,0)




if __name__ == '__main__':
    setup_GPIO()
    speed = int(input("speed: "))
    direction = {'f':forward,
                 'b':backward,
                 'l':left,
                 'r':right}
    cmd = 'go'
    while cmd is not '':
        cmd = input('direction+time: ')
        try: 
            cmd = cmd.split(' ')
            for i in cmd:
                d = i[0]
                t = float(i[1:])
                direction[d](speed, t)
        except:
            print('exiting')
            ''' tidy up '''
            stop()
            GPIO.cleanup()
