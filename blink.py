import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

def start():
     GPIO.output(8, GPIO.HIGH)
     print("Lamba yaniyor")
     
def stop():
     GPIO.output(8, GPIO.LOW)
     print("Lamba sonuyor")

