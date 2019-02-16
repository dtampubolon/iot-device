'''
Created on Jan 19, 2019

@author: Doni Tampubolon

based on lab module 2 guide
'''
import os
from datetime import datetime
from ctypes.test.test_pickling import name

class SensorData():
    
    timeStamp = None #Time when an action is done
    name = 'Temperature Data'
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
        self.name = name
        self.curValue = 0
        self.avgValue = 0
        self.minValue = 0
        self.totValue = 0
        self.sampleCount = 0
        
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
    
    def getAvgValue(self):
        return self.avgValue
    
    def getMaxValue(self):
        return self.maxValue
    
    def getMinValue(self):
        return self.minValue
    
    def getValue(self):
        return self.curValue
    
    def setName(self, name):
        self.name = name
    
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
