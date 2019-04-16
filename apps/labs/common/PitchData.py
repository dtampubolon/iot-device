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
        
    def getValue(self):
        return self.curValue
    
    def setValue(self, newVal):
        self.curValue = newVal
        
    def __str__(self):
        customStr = str(self.name + ' :' + '\n\tTime: ' + self.timeStamp + '\n\tCurrent Value: ' + self.curValue)
        return customStr
    
    def setName(self, name):
        self.name = name