'''
Created on Jan 19, 2019

@author: Doni Tampubolon

based on lab module 2 guide
'''
import os
from datetime import datetime

class SensorData():
    
    #timeStamp = None #Time when an action is done
    #name = 'Temperature Data'
    #curValue = 0 #Current value of reading
    #avgValue = 0 #Average value of readings
    #minValue = 0 #Minimum value of readings
    #maxValue = 0 #Maximum value of readings
    #totValue = 0 #Sum of all the readings
    #sampleCount = 0 #Number of readings taken
    
    '''
    This class keeps track of the maximum, minimum, and average temperature readings
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.timeStamp = str(datetime.now())
        self.name = 'Temperature Sensor'
        self.curValue = 0
        self.avgValue = 0
        self.minValue = 1000000
        self.maxValue = 0
        self.totValue = 0
        self.sampleCount = 0
        
    '''
    This function adds new readings and updates member variables accordingly
    '''
    def addValue(self, newVal):
        self.sampleCount += 1 #increment count
        
        self.timeStamp = str(datetime.now())
        self.curValue = newVal
        self.totValue += newVal
        
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
        
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
            
        if (self.totValue != 0 and self.sampleCount > 0):
            self.avgValue = self.totValue / self.sampleCount
    
    #This function returns the average of all the sensor readings
    def getAvgValue(self):
        return self.avgValue
    
    #This function returns the maximum of all the sensor readings
    def getMaxValue(self):
        return self.maxValue
    
    #This function returns the minimum of all the sensor readings
    def getMinValue(self):
        return self.minValue
    
    #This function returns the current/latest reading
    def getValue(self):
        return self.curValue
    
    #This function returns the name of this SensorData instance
    def setName(self, name):
        self.name = name
    
    #String formatter
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime: ' + self.timeStamp + \
            os.linesep + '\tCurrent: ' + str(self.curValue) + \
            os.linesep + '\tAverage: ' + str(self.avgValue) + \
            os.linesep + '\tSamples: ' + str(self.sampleCount) + \
            os.linesep + '\tMin: ' + str(self.minValue) + \
            os.linesep + '\tMax: ' + str(self.maxValue))
        return customStr
