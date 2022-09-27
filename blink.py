import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
while True:
    GPIO.output(pin, True)
    print("Pin on")
    time.sleep(1)
    GPIO.output(pin, False)
    print("Pin off")
    time.sleep(1)
