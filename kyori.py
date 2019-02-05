# -*- coding: utf-8 -*-

def reading(sensor,TRIG,ECHO):
    import time
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)
    if sensor == 0:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG,GPIO.LOW)
        time.sleep(0.2)

        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == 0:
            signaloff = time.time()
        
        while GPIO.input(ECHO) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
        GPIO.cleanup()
    else:
        print "Inco"

if __name__ == '__main__':
    while True:
        print(reading(0,18,16)+reading(0,18,16))/2
