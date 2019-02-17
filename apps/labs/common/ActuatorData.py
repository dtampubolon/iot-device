'''
Created on Feb 1, 2019

@author: Doni Tampubolon
NUID:001400708
CSYE6530 - Connected Devices
'''
import os

from datetime import datetime
from ctypes.test.test_pickling import name

COMMAND_OFF = 0
COMMAND_ON = 1
COMMAND_SET = 2
COMMAND_RESET = 3

STATUS_IDLE = 0
STATUS_ACTIVE = 1

ERROR_OK = 0
ERROR_COMMAND_FAILED = 1
ERROR_NON_RESPONSIBLE = -1

class ActuatorData():
    '''
    This class contains the appropriate data to signal a temperature increase
    or decrease request
    '''
    timeStamp = None
    name = 'Actuator Name Not set'
    #hasError = False
    #command = 0 #0 to keep temp, 1 to lower temp, 2 to raise temp
    #errCode = 0 
    #statusCode = 0 # 0 for normal, 1 for high temp, 2 for low temp
    #stateData = None
    #val = 0.0 #Value of current data

    def __init__(self):
        '''
        Constructor
        '''
        self.updateTimeStamp()
        self.name = name
        self.hasError = False
        self.command = 0
        self.errCode = 0
        self.statusCode = 0
        self.stateData = None
        self.val = 0.0
    
    #This function returns the value of command
    def getCommand(self):
        return self.command
    
    #This function returns the name of this ActuatorData instance
    def getName(self):
        return self.name
    
    #This function returns the value of stateData
    def getStateData(self):
        return self.stateData
    
    #This function returns the value of statusCode
    def getStatusCode(self):
        return self.statusCode
    
    #This function returns the value of errCode
    def getErrorCode(self):
        return self.errCode
    
    #This function returns the current/latest ActuatorData value
    def getValue(self):
        return self.val
    
    #This returns the boolean value of hasError
    def hasError(self):
        return self.hasError
    
    '''
    This function sets the variable command
    @param command: integer, 0 to keep temp, 1 to lower temp, 2 to raise temp
    '''
    def setCommand(self, command):
        self.command = command
    
    '''
    This funciton sets the name of this ActuatorData instance
    @param name: String
    ''' 
    def setName(self, name):
        self.name = name
        
    '''
    This function sets the value of stateData
    @param stateData: integer
    '''     
    def setStateData(self, stateData):
        self.stateData = stateData
    
    '''
    This function sets the value of statusCode
    @param statusCode: integer,  0 for normal, 1 for high temp, 2 for low temp
    ''' 
    def setStatusCode(self, statusCode):
        self.statusCode = statusCode
    
    '''
    This function sets the value of errCode
    @param errCode: integer
    '''
    def setErrorCode(self, errCode):
        self.errCode = errCode
        
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
    
    '''
    This funciton sets the value of Actuator data
    @param val: float 
    '''        
    def setValue(self, val):
        self.val = val
    
    '''
    This functions copies the values of the variables from an ActuatorData instance
    @param data: ActuatorData
    '''      
    def updateData(self, data):
        self.command = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode = data.getErrorCode()
        self.stateData = data.getStateData()
        self.val = data.getValue()
    
    #This function updates the timeStamp    
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
    
    #String formatter    
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime: ' + self.timeStamp + \
            os.linesep + '\tCommand: ' + str(self.command) + \
            os.linesep + '\tStatus Code: ' + str(self.statusCode) + \
            os.linesep + '\tError Code: ' + str(self.errCode) + \
            os.linesep + '\tState Data: ' + str(self.stateData) + \
            os.linesep + '\tValue: ' + str(self.val))
        return customStr