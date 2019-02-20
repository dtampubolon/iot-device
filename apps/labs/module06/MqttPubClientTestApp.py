'''
Created on Feb 19, 2019

@author: Doni Tampubolon
'''

from labs.module06 import MqttClientConnector
from labs.common import SensorData

class MqttPubClientTestApp(object):
    '''
    Instances of this class publish messages to a connected MQTT broker
    MQTT broker will then publish them to subscribed clients
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        self.topic = "Test-CSYE6530"
        self.payload = "This is a test"
        self.name = "Client1"
        self.connector = MqttClientConnector.MqttClientConnector(self.name)
        self.sensorData = SensorData.SensorData()
    
    def main(self):
        self.connector.connect()
        self.connector.start()
        
    if __name__ == '__main__':
        main()