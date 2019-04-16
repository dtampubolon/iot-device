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


class PitchAdaptor(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.enable = False
        self.sense = SenseHat()
        self.pitchData = PitchData()
        self.curPitch = None
        
    def run(self):
        while True:
            if self.enable:
                self.orientation = self.sense.get_orientation()
                self.curPitch = round(self.orientation["pitch"], 0)
                self.pitchData.setValue(self.curPitch)

    def setEnable(self, enable):
        self.enable = enable
        
    def getCurPitch(self):
        return self.curPitch
    
    def getPitchData(self):
        return self.pitchData