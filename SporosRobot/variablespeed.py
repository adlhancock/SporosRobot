#!/usr/bin/python3

"""
testing pulse width modulation to get variable speed for sporos robot

"""

class variablespeed:

    def __init__(self):
        from SporosRobot import setup
        setup = setup()
        setup.GPIO()
        self.pwm, self.motor_pins = setup.pwm()

    pwm = self.pwm
    p = self.motor_pins
    rfw, rbw, lfw, lbw = (p[key] for key in ('rfw', 'rbw', 'lfw','lbw'))
    
    def stop(self):
        import RPi.GPIO as GPIO
        GPIO.cleanup()
        print("exiting: cleaned up GPIO")

    def go(self):

        """
        returns: 
            left, right, forward, backward, stop
        """
        pwm = self.pwm
        p = self.motor_pins
        rfw, rbw, lfw, lbw = (p[key] for key in ('rfw', 'rbw', 'lfw','lbw'))

        def set_speed(pin,duty):
                pwm[pin].ChangeDutyCycle(duty)
        
        def move(func):
            """ a function wrapper for the different directions """
            def function_wrapper(speed,t):
                from time import sleep as wait
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
            for pin in [rfw,lfw,rbw,lbw]:
                set_speed(pin,0)
                
        # set up dictionary of abbreviations for movement functions
        direction = {'f':forward,
                     'b':backward,
                     'l':left,
                     'r':right}

        # set the speed
        speed = int(input("set speed:"))
        
        # it doesn't really matter what `cmd` starts out as 
        # as long as it isn't an empty string
        cmd_string = 'go'

        while cmd_string is not '':
            cmd_string = input('direction+time: ')
            try: 
                commands = cmd_string.split(' ')
                for i in commands:
                    d = i[0]
                    t = float(i[1:])
                    direction[d](speed, t)
            except:
                print('no command entered')
                ''' tidy up '''
                stop()
        return

if __name__ == '__main__':
    # import SporosRobot

    sporos = variablespeed()
    sporos.go()
    sporos.stop()

    """
    setup_GPIO()
    pwm = setup_pwm()
    speed = int(input('speed: '))
    l,r,f,b,stop,go = directions(pwm)
    go()
    GPIO.cleanup()
    """
