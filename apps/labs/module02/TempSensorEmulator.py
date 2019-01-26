'''
Created on Jan 19, 2019

@author: Doni Tampubolon
NUID: 001400708
CSYE 6530 - Connected Devices
Lab Module 2
'''
import threading
import time
from random import uniform
from labs.common import SensorData

class TempSensorEmulator(threading.Thread):
    '''
    This class emulates a real temperature sensor by 
    generating a random value between 0 - 30 degrees Celsius
    '''
    
    def __init__(self, period, threshold, connector):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.connector = connector
        self.period = period #time interval in seconds
        self.threshold = threshold #Threshold that triggers app to send an alert to user
        self.minVal = 0 #Minimum temperature value in Celsius
        self.maxVal = 30 #Maximum temperature value in Celsius
        self.enable = False
        self.sensorData = SensorData.SensorData()
        self.isPrevTempSet = False #Before the sensor emulator is started, no previous temperature readings i.e. no average temp
    
    def run(self):
        while True:
            if self.enable:
                self.curTemp = uniform(float(self.minVal), float(self.maxVal))
                self.sensorData.addValue(self.curTemp)
                
                print("\n----------")
                print("New Sensor Readings")
                print(" " + str(self.sensorData))
                
                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp #Initial temp is set to the first current temp
                    self.isPrevTempSet = True
                else:
                    if(abs(self.curTemp - self.sensorData.getAvgValue()) >= self.threshold):
                        print("\n Current temperature exceeds average by :"  + str(self.threshold))
                        print("Sending email alert...")
                        
                    self.connector.publishMessage("Exceptional sensor data ", self.sensorData)
                    time.sleep(self.period)
                    
    def setEnable(self, enable):
        self.enable = enable