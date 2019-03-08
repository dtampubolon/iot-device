'''
Created on Mar 7, 2019

@author: Doni Tampubolon
'''

from labs.common import DataUtil
from labs.common import SensorData
from labs.common import ConfigConst

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

class CoapClientConnector(object):
    '''
    classdocs
    '''


    def __init__(self, host = ConfigConst.DEFAULT_HOST, isSecure = False):
        '''
        Constructor
        '''
        self.host = host
        self.payload = "";
        self.uri = None #Last accessed URI
        
        self.sensorData = SensorData.SensorData()
        self.dataUtil = DataUtil.DataUtil( r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\CoAPClientData.json')

        if(isSecure):
            self.port = ConfigConst.SECURE_COAP_PORT
        else:
            self.port = ConfigConst.DEFAULT_COAP_PORT
        
        self.client = HelperClient(server=(self.host,self.port))

        self.response = ""
        
    def sendGetRequest(self, uri):
        self.uri = uri
        host, port, path = parse_uri(uri)
        response = self.client.get(path)
        print(response.pretty_print())
        self.client.stop()
        
    def sendPutRequest(self, uri, payload):
        self.uri = uri
        self.payload = payload
        host, port, path = parse_uri(uri)
        response = self.client.put(path, payload)
        print("\nResponse from server:")
        print((response.pretty_print()))
        self.client.stop()
        
    def sendPostRequest(self, uri, payload):
        self.uri = uri
        self.payload = payload
        host, port, path = parse_uri(uri)
        response = self.client.post(path, payload)
        print((response.pretty_print()))
        self.client.stop()
                
    def sendDeleteRequest(self, uri):
        self.uri = uri
        host, port, path = parse_uri(uri)
        response = self.client.delete(path)
        print(response.pretty_print())
        
    def sendObserveRequest(self, uri):
        self.uri = uri
        host, port, path = parse_uri(uri)
        self.response = self.client.observe(path, client_callback_observe)
        
    def CancelObserve(self):
        self.client.cancel_observing(self.response, True)
    
    def sendDiscoverRequest(self):
        response = self.client.discover()
        print("\nResponse from server:")
        print(response.pretty_print())
        print("Stopping Client...")
        self.client.stop()
    
    def stopClient(self):
        self.client.stop()
'''
Callback functions
'''
def client_callback_get(response):
    print("GET callback:\t" + str(response))
    
def client_callback_observe(response):
    #Called every time there's a new notification from observed path
    print("OBSERVE callback:\t" + str(response))
    
def client_callback_delete(response):
    print("DELETE callback:\t" + str(response))