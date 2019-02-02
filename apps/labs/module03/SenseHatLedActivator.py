'''
Created on Feb 1, 2019

@author: Doni Tampubolon
'''
from time import sleep
from sense_hat import SenseHat
import threading

class SenseHatLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
            
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
        
    def run(self):
        while True:
            if self.enableLed:
                if self.displayMsg != None:
                    self.sh.show_message(str(self.displayMsg))
                    self.setDisplayMessage(None)
                else:
                    self.sh.show_message(str('R'))
                    
                sleep(self.rateInSec)
                self.sh.clear()
                
            sleep(self.rateInSec)
        
    def getRateInSeconds(self):
        return self.rateInSec
    
    def setEnableLeddFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
        
    def setDisplayMessage(self,msg):
        self.displayMsg = msg