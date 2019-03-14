'''
Created on Mar 7, 2019

@author: Doni Tampubolon
'''
from labs.module07.CoapClientConnector import CoapClientConnector
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil

class CoapClientTestApp():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.host = "127.0.0.1"
        self.port = 5683
        self.multicast = False
        self.connector = CoapClientConnector(self.host)
        self.sd = SensorData()
        self.du = DataUtil(r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\coapclientSD.json')
    
if __name__ == '__main__':
    #Create app instance
    clientApp = CoapClientTestApp()
    
    #Adding test values to sensor data
    clientApp.sd.addValue(31.8)
    clientApp.sd.addValue(23.5)
    clientApp.sd.addValue(26.9)
    
    #Converting sensor data to JSON
    jsonData = clientApp.du.sensorDataToJson(clientApp.sd)
    print("Client SensorData JSON before transmission to server:")
    print(jsonData)
    
    #Send DISCOVER request
    #clientApp.connector.sendDiscoverRequest()
    
    #Send PUT request
    clientApp.connector.sendPostRequest("coap://127.0.0.1:5683/json", jsonData)
    clientApp.connector.sendGetRequest("coap://127.0.0.1:5683/json")
    #clientApp.connector.sendDiscoverRequest()

    #Stop client
    clientApp.connector.stopClient()