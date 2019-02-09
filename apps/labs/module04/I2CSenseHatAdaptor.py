'''
Created on Feb 6, 2019

@author: Doni Tampubolon
'''
import sys
#sys.path.append('/home/pi/workspace/iot-device/apps')

import threading
import smbus

from time import sleep

from labs.common import ConfigUtil
from labs.common import ConfigConst

i2cBus  = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3+

enableControl = 0x2D
enableMeasure = 0x08

accelAddr = 0x1C # Address for IMU (Accelerometer)
magAddr = 0x6A # Address for IMU (Magnetometer)
pressAddr = 0x5C # Address for pressure sensor
humidAddr = 0x5F # Address for humidity sensor

begAddr = 0x28 # beginning address
totBytes = 6 # total number of bytes

DEFAULT_RATE_IN_SEC = 5 # Interval in seconds between new data readings

class I2CSenseHatAdaptor(threading.Thread):
    '''
    This class is an adaptor for a device (sensor/actuator) that connects via I2C
    With this class, bytes of data can be written and/or read via I2C
    '''
    rateInSec = DEFAULT_RATE_IN_SEC

    def __init__(self):
        '''
        Constructor
        '''
        super(I2CSenseHatAdaptor, self).__init__()
        
        self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
        
        print("Configuration data...\n" + str(self.config))
        
        self.enableEmulator = False
        
        self.initI2CBus()
        
    def initI2CBus(self):
        print("Initializing I2C bus and enabling I2C addresses...")
        
        i2cBus.write_quick(accelAddr)
        i2cBus.write_quick(magAddr)
        i2cBus.write_quick(pressAddr)
        i2cBus.write_quick(humidAddr)
        
    def run(self):
        while True:
            if self.enableEmulator:
                self.displayAccelerometerData()
                self.displayMagnetometerData()
                self.displayPressureData()
                self.displayHumidityData()
                
            sleep(self.rateInSec)
         
    def displayAccelerometerData(self):
        '''
        Read data from accelerometer and display it in console
        '''
        data = i2cBus.read_i2c_block_data(accelAddr, 0x28, 6)
        print("Accelerometer block data: {}".format(data))
    
    
    def displayMagnetometerData(self):
        '''
        Read data from magnetometer and display it in console
        '''
        data = i2cBus.read_i2c_block_data(magAddr, 0x28, 24)
        print("Magnetometer block data: {}".format(data))
    
    def displayPressureData(self):
        '''
        Read data from pressure sensor and display it in console
        '''
        lsb = i2cBus.read_i2c_block_data(pressAddr, 0x28,1)
        middlebits = i2cBus.read_i2c_block_data(pressAddr, 0x29,1)
        msb = i2cBus.read_i2c_block_data(pressAddr, 0x2A,1)
        print("Pressure block data: {}{}{}".format(msb,middlebits,lsb))
        
    def displayHumidityData(self):
        '''
        Read data from humidity sensor and display it in console
        '''
        lsb = i2cBus.read_i2c_block_data(humidAddr, 0x28,1)
        msb = i2cBus.read_i2c_block_data(pressAddr, 0x28,1)
        print("Humidity block data: {}{}".format(msb,lsb))       
    
    def setEnable(self, enable):
        self.enableEmulator = enable