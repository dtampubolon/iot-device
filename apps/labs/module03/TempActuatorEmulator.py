'''
Created on Feb 1, 2019

@author: Doni Tampubolon
NUID: 001400708
CSYE 6530 - Connected Devices
Lab Module 3
'''

from sense_hat import SenseHat
from labs.common import ActuatorData

class TempActuatorEmulator():
    '''
    This class determines if the temperature has to be raised or lowered.
    This class will then send the appropriate signal to GPIO (SenseHat).
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.sense = SenseHat()
        self.prevActuatorData = ActuatorData.ActuatorData() #Create a default actuator data instance
        self.prevActuatorDataIsSet = True
        
    def processMessage(self, actuatorData):
        if self.prevActuatorDataIsSet == False: #Check if Actuator Data has been set
            self.prevActuatorDataIsSet = True
            self.prevActuatorData = actuatorData
        
        else: #Compare own actuatorData with actuatorData from argument
            if self.prevActuatorData.timeStamp != actuatorData.timeStamp:
                tempDiff = abs(actuatorData.getValue() - 20)
                print("Actuate thermostat...")                       
                if(actuatorData.getCommand() == 1):
                    self.sense.show_message("TEMP WILL BE LOWERED by " + str(tempDiff))
                elif(actuatorData.getCommand() == 2):
                    self.sense.show_message("TEMP WILL BE RAISED by " + str(tempDiff))
               
                self.prevActuatorData = actuatorData
            