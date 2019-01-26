'''
Created on Jan 19, 2019
Lab Module 2
@author: Doni Tampubolon
NUID: 001400708
CSYE6530 - Connected Devices

This module simulates an app that runs the sensor emulators and connect to an SMTP client connector
'''

from time import sleep
from labs.module02 import TempSensorEmulator
from labs.module02 import SmtpClientConnector

'''
Create and run Temperature Sensor Emulator thread
'''
smtpConnector = SmtpClientConnector.SmtpClientConnector()
tempSE = TempSensorEmulator.TempSensorEmulator(20,5,smtpConnector)
tempSE.daemon = True #Runs thread as a background task
tempSE.setEnable(True)
tempSE.start()

'''
Run app indefinitely
'''
while (True):
    sleep(5)
    pass
