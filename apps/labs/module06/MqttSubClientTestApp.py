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
        self.name = "Subscriber"
        self.connector = MqttClientConnector.MqttClientConnector("CSYE6530-Subscriber")
        self.sensorData = SensorData.SensorData()
        self.dataUtil = DataUtil(r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\test2.json')       

if __name__ == '__main__':
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
    
    #Convert received JSON string to SensorData
        