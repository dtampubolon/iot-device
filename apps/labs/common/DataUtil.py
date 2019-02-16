'''
Created on Feb 15, 2019

@author: Doni Tampubolon
'''
import os
import json
from labs.common import ActuatorData
from labs.common import SensorData

class DataUtil():
    '''
    This class converts data from and to JSON strings
    '''
    dataPath = r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data'
    dataFile = dataPath + '\\' +  'Data.json'
    isLoaded   = False
    
    def __init__(self, dataFile):
        '''
        Constructor for DataUtil
        '''
        if (dataFile != None):
            self.dataFile = dataFile
            
    '''
    Attempts to load the config file using the name passed into
    the constructor.
    
    @param dataFile The name of the data file to load.
     
    '''
    def loadData(self):
        print(str(os.listdir(self.dataPath)))
        
        if (os.path.exists(self.dataPath)):
            print("Loading data from: " + self.dataFile)
            self.isLoaded = True
        else:
            print("Failed to OS-check data. Will try to load: " + self.dataFile)
            self.isLoaded = True
                
    '''
    This method converts from JSON into an ActuatorData object
    '''
    def jsonToActuatorData(self, dataFile):
        with open(dataFile, encoding='utf-8') as jsonData:
            adDict = json.loads(jsonData.read())
        
        print(" decode [pre] --> " + str(adDict))
        
        ad = ActuatorData.ActuatorData()
        ad.name = adDict['name']
        ad.timeStamp = adDict['timeStamp']
        ad.hasError = adDict['hasError']
        ad.command = adDict['command']
        ad.errCode = adDict['errCode']
        ad.statusCode = adDict['statusCode']
        ad.stateData = adDict['stateData']
        ad.curValue = adDict['curValue']
        
        print(" decode [post] --> "+ str(ad))
        
        return ad
    
    '''
    This method converts from JSON into a SensorData object

    '''
    def jsonToSensorData(self, dataFile):
        with open(dataFile, encoding='utf-8') as jsonData:
            sdDict = json.loads(jsonData.read())
        
        print(" decode [pre] --> " + str(sdDict))
        
        sd = SensorData.SensorData()
        sd.name = sdDict['name']
        sd.timeStamp = sdDict['timeStamp']
        sd.avgValue = sdDict['avgValue']
        sd.minValue = sdDict['minValue']
        sd.maxValue = sdDict['maxValue']
        sd.curValue = sdDict['curValue']
        sd.totValue = sdDict['totValue']
        sd.sampleCount = sdDict['sampleCount']
        
        print(" decode [post] --> " + str(sd))
        
        return sd
    
    '''
    This method converts an ActuatorData object into JSON string
    JSON string is written to a file specified by dataFile
    
    @param ActuatorData object to be converted
    '''
    def actuatorDataToJson(self, actuatorData):
        print("Converting ActuatorData:" + str(actuatorData) + " to JSON...")
        jsonOut = json.dumps(actuatorData.__dict__)
        
        return jsonOut
    '''
    This method converts an ActuatorData object into JSON string
    JSON string is written to a file specified by dataFile
    
    @param SensorData object to be converted
    '''    
    def sensorDataToJson(self, sensorData):
        print("Converting SensorData: " + str(sensorData.name) + " to JSON...")
        jsonOut = json.dumps(sensorData.__dict__)   

        return jsonOut