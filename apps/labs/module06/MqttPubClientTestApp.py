'''
Created on Feb 19, 2019

@author: Doni Tampubolon
'''

from labs.module06 import MqttClientConnector
from labs.common import SensorData
from labs.common.DataUtil import DataUtil

class MqttPubClientTestApp():
    '''
    Instances of this class publish messages to a connected MQTT broker
    MQTT broker will then publish them to subscribed clients
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.topic = "Topic-CSYE6530"
        self.payload = "This is a test"
        self.name = "CSYE6530PythonPublisher"
        self.connector = MqttClientConnector.MqttClientConnector("CSYE6530-Publisher")
        self.sensorData = SensorData.SensorData()
        self.dataUtil = DataUtil(r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\publisher.json')
       
if __name__ == '__main__':
    #Create Test app instance
    PubClientApp = MqttPubClientTestApp()
        
    #Adding test values to sensorData
    PubClientApp.sensorData.addValue(31.8)
    PubClientApp.sensorData.addValue(23.5)
    PubClientApp.sensorData.addValue(22.1)
    PubClientApp.sensorData.addValue(25.5)
    PubClientApp.sensorData.addValue(26.9)
    
    #Converting sensorData to JSON
    jsonData = PubClientApp.dataUtil.sensorDataToJson(PubClientApp.sensorData)
    print("Conversion to JSON result: " + jsonData)
    
    PubClientApp.payload = jsonData
    
    #Connect to MQTT broker 
    PubClientApp.connector.connect("iot.eclipse.org",1883)
    
    #publishing data to MQTT broker
    print(PubClientApp.name + " publishing data to broker...")
    PubClientApp.connector.publish(PubClientApp.topic, PubClientApp.payload)
    PubClientApp.connector.run(100)
    
    print("End of Phyton Publisher app")

    
   