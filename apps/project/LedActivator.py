'''
Created on Feb 1, 2019

@author: Doni Tampubolon
'''
from time import sleep
from sense_hat import SenseHat
import threading

import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

class LedActivator():
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    color = [255,165,0]
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
            
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)

    def setLED(self, enable):
        if(enable):
            self.sh.show_letter('*', self.color)
            print("Valve ON")
        else:
            self.sh.clear()
            print("Valve OFF")
        