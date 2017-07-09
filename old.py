import RPi.GPIO as GPIO
import time

import RPi.GPIO as GPIO
import time
import config
GPIO.setmode(GPIO.BOARD)
#button1 = 18
#button2 = 22
#light = 16
#controlPin = [7,11,13,15]

#for i in range(512):
#       for halfstep in range(4):
#               for pin in range(4):
#                       GPIO.output(ControlPin[pin], seq[halfstep][pin])
#               time.sleep(sleepTime
"""
def spin(step):
        seq= [  [1,1,0,0],
                [0,1,1,0],
                [0,0,1,1],
                [1,0,0,1] ]
        #step one step
#       print seq[step]
        for pig in range(4):
                GPIO.output(config.controlPin[pig], seq[step][pig])
        time.sleep(config.sleepTime)
def init():
        #Light = 16

        bottonPresed = False
        for pin in config.controlPin:
                GPIO.setup(pin,GPIO.OUT)
                GPIO.output(pin,0)
        GPIO.setup(config.button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(config.light,GPIO.OUT)
        GPIO.output(config.light,1)

        try:
                while bottonPresed == False:
                        input_state = GPIO.input(config.button1)
                        if input_state == False:
                                bottonPresed = True
                                time.sleep(0.2)
                                main("D")
                        input_state = GPIO.input(config.button2)
                        if input_state == False:
                                bottonPresed = True
                                time.sleep(0.2)
                                main("C")
        except KeyboardInterrupt:
                GPIO.cleanup()
                quit()

#direction = raw_input("C for clockwise D for Declockwise ")

def main(direction):
        sleepTime = 0.010
        step = 0

        try:
                while True:
                        input_state = GPIO.input(config.button1)
                        if input_state == False:
                                if config.sleepTime > 0.002:
                                        config.sleepTime = config.sleepTime - 0$
                                        print('speed incresed')
                                print(config.sleepTime)
                        input_state1 = GPIO.input(config.button2)
                        if input_state1 == False:
                                if config.sleepTime < 100:
                                        config.sleepTime = config.sleepTime + 0$
                                        print('speed decresed')
                                print(config.sleepTime)
                        if input_state == False and input_state1 == False:
                                print("bubbelt upp")
                                time.sleep(0.5)
                                init()
                        spin(step)
                        GPIO.output(config.light, 0)
                        if direction == "D":
                                if step == 0:
                                        step = 3
                                else:
                                        step -=1
                        else:
                                if step == 3:
                                        step = 0
                                else:
                                        step +=1

        except KeyboardInterrupt:
                GPIO.cleanup()
init()

"""