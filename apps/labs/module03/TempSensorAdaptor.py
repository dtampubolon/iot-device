'''
Created on Jan 19, 2019

@author: Doni Tampubolon
NUID: 001400708
CSYE 6530 - Connected Devices
Lab Module 3
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

import threading
import time

from labs.common import SensorData
from labs.common import ActuatorData
from labs.common import ConfigConst
from labs.common import ConfigUtil
from sense_hat import SenseHat

class TempSensorAdaptor(threading.Thread):
    '''
    This class reads temperature data from sensehat
    and sends email notifications if changes beyond the threshold occur. 
    '''
    
    def __init__(self, period, threshold, connector, actuatorEmu):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.connector = connector
        self.period = period #time interval in seconds
        self.threshold = threshold #Threshold that triggers app to send an alert to user
        self.enable = False
        self.sense = SenseHat()
        
        self.sensorData = SensorData.SensorData()
        self.actuatorEmu = actuatorEmu #ActuatorEmulator instance
        
        
        self.isPrevTempSet = False #Before the sensor adaptor is started, no previous temperature readings i.e. no average temp
        
        self.config = ConfigUtil.ConfigUtil(r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        
        self.nominalTemp = float(self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.NOMINAL_TEMP_KEY))

        
    def run(self):
        while True:
            if self.enable:
                self.curTemp = self.sense.get_temperature()
                self.sensorData.addValue(self.curTemp)
                
                print("\n----------")
                print("New Sensor Readings")
                print(" " + str(self.sensorData))
                
                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp #Initial temp is set to the first current temp
                    self.isPrevTempSet = True
                else:
                    if(abs(self.curTemp - self.sensorData.getAvgValue()) >= self.threshold):
                        print("\n Current temperature differs from average by :"  + str(self.threshold))
                        print("Sending email alert...")
                        self.connector.publishMessage("Exceptional sensor data", self.sensorData)
                        
                        actuatorData = ActuatorData.ActuatorData()

                        if self.curTemp > self.nominalTemp:
                            #Filling out actuator data and pass them to TempActuatorEmulator.
                            actuatorData.updateTimeStamp()
                            actuatorData.setCommand(1)
                            actuatorData.setStatusCode(1)
                            actuatorData.setErrorCode(0)                        
                            actuatorData.setStateData("HIGH")
                            actuatorData.setValue(self.curTemp)
                                
                            self.actuatorEmu.processMessage(actuatorData)
                    
                            
                        elif self.curTemp < self.nominalTemp:
                            actuatorData.updateTimeStamp()
                            actuatorData.setCommand(2)
                            actuatorData.setStatusCode(2)
                            actuatorData.setErrorCode(0)                        
                            actuatorData.setStateData("LOW")
                            actuatorData.setValue(self.curTemp) 
                                
                            self.actuatorEmu.processMessage(actuatorData)
                        
                        actuatorData.setStatusCode(0)
                time.sleep(self.period)
                    
    def setEnable(self, enable):
        self.enable = enable