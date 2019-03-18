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
    This class is used to create a CoAP client instance
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
    
    '''
    This function is called when a client wants to sent a GET request to the server
    '''
    def sendGetRequest(self, uri):
        self.uri = uri
        host, port, path = parse_uri(uri)
        response = self.client.get(path, client_callback_get)
        print("\nResponse from server:")
        print(response.pretty_print())
        #self.client.stop()
     
    '''
    This function is called when a CoAP client wants to PUT a payload into a CoAP server
    '''    
    def sendPutRequest(self, uri, payload):
        self.uri = uri
        self.payload = payload
        host, port, path = parse_uri(uri)
        response = self.client.put(path, payload)
        print("\nResponse from server:")
        print((response.pretty_print()))
        #self.client.stop()
     
    '''
    This function is called when a CoAp client wants to POST a payload into a CoAP server
    '''   
    def sendPostRequest(self, uri, payload):
        self.uri = uri
        self.payload = payload
        host, port, path = parse_uri(uri)
        response = self.client.post(path, payload)
        print((response.pretty_print()))
        #self.client.stop()
    
    '''
    This function is called when a CoAP client wants to delete a resource in a CoAP server
    '''            
    def sendDeleteRequest(self, uri):
        self.uri = uri
        host, port, path = parse_uri(uri)
        response = self.client.delete(path, client_callback_delete)
        print(response.pretty_print())
        #self.client.stop()
    
    '''
    This function is used when a CoAP client wants to observe a particular resource in a CoAP server
    '''    
    def sendObserveRequest(self, uri):
        self.uri = uri
        host, port, path = parse_uri(uri)
        self.response = self.client.observe(path, client_callback_observe)
    
    '''
    This function is called when a CoAP client wants to stop observing a resource in a CoAP server
    '''    
    def CancelObserve(self):
        self.client.cancel_observing(self.response, True)
    
    '''
    This function is called by a CoAP client to discover the resources available in a CoAP server
    '''
    def sendDiscoverRequest(self):
        response = self.client.discover()
        print("\nResponse from server:")
        print(response.pretty_print())
        print("Stopping Client...")
        #self.client.stop()
    
    '''
    This function is used to stop running CoAP client
    '''
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