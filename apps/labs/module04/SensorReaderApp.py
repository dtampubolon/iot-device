'''
Created on Feb 7, 2019
@author: Doni Tampubolon
NUID: 001400708
CSYE6530 - Connected Devices
Lab Module 4

This module simulates an app that manages the sensors and actuators via I2C connection
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

from time import sleep
from labs.module04 import I2CSenseHatAdaptor


'''
Create and run sensor adaptor instance via I2C
'''
I2CSHA = I2CSenseHatAdaptor.I2CSenseHatAdaptor()
I2CSHA.daemon = True #Runs thread as a background task
I2CSHA.setEnable(True)
I2CSHA.start()

'''
Run app indefinitely
'''
while (True):
    sleep(5)
    pass
