import easygopigo3 as easy
from di.sensors.easy_distance_sensor import EasyDistanceSensor
import time
import random
from time import sleep

gpg = easy.EasyGoPiGo3()
my_sensor = EasyDistanceSensor()

def loop():
  run = True
  
  while run:
    gpg.drive_cm(20)
    left_or_right = random.randrange(1,4)
    
    read_distance = my_sensor.read()
    print("Distance from object: {} (cm): ".format(read_distance))
    
    # This is where it scans if it's to close
    if my_sensor.read() <= 25:
      gpg.drive_cm(-30)
       
       gpg.turn_degrees(90)
       right_read_distance = my_sensor.read()
       
       gpg.turn_degrees(180)
       left_read_distance = my_sensor.read()
       
       gpg.turn_degrees(90)
       
       time.sleep(0.1)
       
       if right_read_distance > left_read_distance:
         print("Right it is.")
         gpg.turn_degrees(90)
        
       if left_read_distance > right_read_distance:
         print("Left it is.")
         gpg.turn_degrees(-90)
         
       if left_read_distance == left_read_distance:
         if left_or_right >= 2:
           print("I don't care, left")
           gpg.turn_degrees(-90)
           
         else:
           print("I don't care, right")
           gpg.turn_degrees(90)
   
loop()
