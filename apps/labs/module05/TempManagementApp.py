'''
Created on Feb 15, 2019
@author: Doni Tampubolon
NUID: 001400708
CSYE6530 - Connected Devices
Lab Module 5

This module simulates an app that runs the sensor adaptors, actuators, and
connect to an SMTP client connector
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

from time import sleep
from labs.module05 import TempSensorAdaptor
from labs.module03 import TempActuatorEmulator
from labs.module03 import SmtpClientConnector
from labs.common import DataUtil
'''
Create and run Temperature Sensor Adaptor thread and SMTP client connector
'''
smtpConnector = SmtpClientConnector.SmtpClientConnector()
tempAE = TempActuatorEmulator.TempActuatorEmulator()
tempSA = TempSensorAdaptor.TempSensorAdaptor(20,2,smtpConnector,tempAE)
tempSA.daemon = True #Runs thread as a background task
tempSA.setEnable(True)
tempSA.start()
#DU = DataUtil.DataUtil(r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\Data.json')

'''
Run app indefinitely
'''
while (True):
    #DU.jsonToSensorData(r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\Data.json')
    sleep(5)
    pass
