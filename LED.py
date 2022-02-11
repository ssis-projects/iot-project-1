# This is a script to test if the breadboard
# is connected properly to the Raspberry Pi.

import RPi.GPIO as GPIO
import time

OUTPUT_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)

print("LED on")

GPIO.output(OUTPUT_PIN, GPIO.HIGH)
time.sleep(1)

print("LED off")

GPIO.output(18, GPIO.LOW)