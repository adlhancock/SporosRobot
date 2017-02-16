#! /usr/bin/python3

""" SporosRobot's bat eyes!

"""

import RPi.GPIO as GPIO
import time


pinTrigger = 17
pinEcho = 18

def setup_ears():
    """ setup pins required for distance measurement
    
    Actions
    ^^^^^^^
    - sets mode as BCM
    - set sets warnings off
    - sets trigger and echo pins as output and input respectively

    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)


def get_distance():
    """ Gets distance once using ultrasonic pulse

    Parameters:
    -----------
        None
    Returns:
    --------
        distance in cm

    """
    
    GPIO.output(pinTrigger, False) # pulse off
    time.sleep(0.2)

    GPIO.output(pinTrigger,True) # send 10us pulse
    time.sleep(10e-6)
    GPIO.output(pinTrigger,False)

    StartTime = time.time()     # start timer

    while GPIO.input(pinEcho)==0: # keep timer reset
        StartTime = time.time()

    while GPIO.input(pinEcho) == 1:
        StopTime = time.time()

        if StopTime - StartTime >= 0.04:
            print("Too close!!!")
            StopTime = StartTime
            break

    ElapsedTime = StopTime - StartTime

    distance = (ElapsedTime * 34326)/2

    print('{:2.1f} cm'.format(distance))
    #dots = int(distance/2)
    #print('.'*dots)

    return(distance)


if __name__ == "__main__":

    setup_ears()
    try:

        while True:
            d = get_distance()
            time.sleep(0.1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\n\nclean exit")

