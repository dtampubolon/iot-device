'''
Created on Feb 19, 2019

@author: Doni Tampubolon
'''
from labs.module06 import MqttClientConnector
from labs.common import SensorData
from labs.common.DataUtil import DataUtil

class MqttSubClientTestApp():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.topic = "Topic-CSYE6530"
        self.payload = "This is a test"
        self.name = "CSYE6530PythonSubscriber"
        self.dataFile = r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\received-data.json'
        self.connector = MqttClientConnector.MqttClientConnector("CSYE6530-Subscriber")
        self.sensorData = SensorData.SensorData()
        self.dataUtil = DataUtil(self.dataFile)       

if __name__ == '__main__':
    
    print("Running subscriber...\n")
    #Create app instance
    subApp = MqttSubClientTestApp()
    
    #Connect to MQTT broker
    subApp.connector.connect()
    
    #Subscribing to a topic
    subApp.connector.subscribe(subApp.topic, 2)
    subApp.connector.run(120)
    
    #Get data from subscription
    if(subApp.connector.payload != None):
        jsonData = subApp.connector.payload.decode()
        print("Received JSON string: " + jsonData)
        with open(subApp.dataFile,"w") as outFile:
            print(jsonData, file = outFile)
        
    #Convert received JSON string to SensorData
        subApp.sensorData = subApp.dataUtil.jsonToSensorData(subApp.dataFile)
        
    #Convert reconstituted SensorData back to JSON String
        print(subApp.dataUtil.sensorDataToJson(subApp.sensorData))
        
    #Unsubscribe from topic
    subApp.connector.unsubscribe(subApp.topic)
    
    #Disconnect from broker
    subApp.connector.disconnect()