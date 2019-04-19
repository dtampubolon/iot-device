'''
Created on Jan 19, 2019

@author: Doni Tampubolon
NUID: 001400708
CSYE 6530 - Connected Devices
Final Project
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

import threading
import time

from labs.common import SensorData
from labs.common import ConfigConst
from labs.common import ConfigUtil
from labs.common import DataUtil
from labs.module06 import MqttClientConnector
from sense_hat import SenseHat

class TempSensorAdapt(threading.Thread):
    '''
    This class reads temperature data from sensehat
    and sends email notifications if changes beyond the threshold occur. 
    '''
    def __init__(self, connector, period=1, threshold=25):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.period = period #time interval in seconds
        self.threshold = threshold #Threshold that triggers app to send an alert to user
        self.enable = False
        self.sense = SenseHat()
        self.pubTopic = "Temperature-CSYE6530"
        self.sensorData = SensorData.SensorData()
        self.connector = connector #MQTT connector
        
        self.isPrevTempSet = False #Before the sensor adaptor is started, no previous temperature readings i.e. no average temp
        
        self.config = ConfigUtil.ConfigUtil()
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        
        self.nominalTemp = float(self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.NOMINAL_TEMP_KEY))
        self.dataUtil = DataUtil.DataUtil()
        
    def run(self):
        while True:
            if self.enable:
                self.curTemp = self.sense.get_temperature()
                self.sensorData.addValue(self.curTemp)
                
                #print("\n----------")
                #print("New Sensor Readings")
                #print(" " + str(self.sensorData))
                
                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp #Initial temp is set to the first current temp
                    self.isPrevTempSet = True
                else:
                    if(self.curTemp>=self.threshold):
                        print("ALERT: Temperature exceeds the maximum!")
                        self.connector.publish(self.pubTopic)
                time.sleep(self.period) #sleep for 1 second in every loop
                    
    def setEnable(self, enable):
        self.enable = enable
        
    def getSensorData(self):
        return self.sensorData