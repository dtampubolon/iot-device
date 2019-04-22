'''
Created on Apr 15, 2019

@author: Doni Tampubolon
'''

import os
from datetime import datetime

class PitchData(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.timeStamp = str(datetime.now())
        self.name = 'Pitch Orientation Sensor'
        self.curValue = 0
        
    #This function returns the current value
    def getValue(self):
        return self.curValue
    
    #This function sets the current value
    def setValue(self, newVal):
        self.curValue = newVal
    
    #This function is a string formatter for this object    
    def __str__(self):
        customStr = str(self.name + ' :' + '\n\tTime: ' + self.timeStamp + '\n\tCurrent Value: ' + self.curValue)
        return customStr
    
    #This function sets the name of this object
    def setName(self, name):
        self.name = name