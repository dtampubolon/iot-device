'''
Created on Apr 15, 2019

@author: Doni Tampubolon
'''

import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

import threading
import time

from labs.common.PitchData import PitchData
from labs.common import ConfigConst
from labs.common import ConfigUtil
from sense_hat import SenseHat
from labs.module06 import MqttClientConnector
from labs.common import DataUtil

'''
This class takes pitch readings from SenseHat's gyroscope module
'''
class PitchAdaptor(threading.Thread):
    '''
    Constructor
    '''
    def __init__(self):
        threading.Thread.__init__(self)
        self.enable = False
        self.sense = SenseHat()
        self.pitchData = PitchData()
        self.curPitch = None
    
    '''
    This function is called when a PitchAdaptor thread is started. It constantly gets a new pitch reading from SenseHat
    '''    
    def run(self):
        while True:
            if self.enable:
                self.orientation = self.sense.get_orientation()
                self.curPitch = round(self.orientation["pitch"], 0)
                self.pitchData.setValue(self.curPitch)
    
    '''
    This function enables the run function
    '''
    def setEnable(self, enable):
        self.enable = enable
    
    '''
    This function returns the current value of pitch
    '''    
    def getCurPitch(self):
        return self.curPitch
    
    '''
    This function returns the latest pitchData object
    '''
    def getPitchData(self):
        return self.pitchData