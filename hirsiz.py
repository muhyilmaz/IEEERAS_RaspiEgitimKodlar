import time 
import RPi.GPIO as io 
io.setmode(io.BCM) 

pir_pin = 18 
door_pin = 23 

io.setup(pir_pin, io.IN) # activate input 
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP) # activate input with PullUp 
while True: 
  if io.input(pir_pin): 
    print(“HAREKET ALARMI!”) 
  if io.input(door_pin): 
    print(“KAPI ALARMI!”) 
  time.sleep(0.5)
