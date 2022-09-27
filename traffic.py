import RPi.GPIO as GPIO
import time

green1 = 21
blue1 = 16
yellow1 = 12
red1 = 24

green2 = 3
blue2 = 5
yellow2 = 7
red2 = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, False)
GPIO.output(yellow, False)
GPIO.output(green, False)
GPIO.output(blue, False)
while True:
    GPIO.output(green, True)
    GPIO.output(blue, True)
    print("Green and blue on")
    time.sleep(2)
    GPIO.output(blue, False)
    print("blue off")
    time.sleep(2)
    GPIO.output(green, False)
    GPIO.output(yellow, True)
    print("green off, yellow on")
    time.sleep(1.5)
    GPIO.output(yellow, False)
    GPIO.output(red, True)
    print("yellow off, red on")
    time.sleep(4) #How long?
    GPIO.output(red, False)
    print("red off")
