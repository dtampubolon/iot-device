'''
Created on Mar 7, 2019

@author: Doni Tampubolon
'''
from coapthon.server.coap import CoAP
from labs.common import ConfigConst
class CoapServerConnector():
    '''
    This class is used to connect to 
    '''

    def __init__(self, host = ConfigConst.DEFAULT_HOST, port=ConfigConst.DEFAULT_COAP_PORT, multicast=False):
        '''
        Constructor
        '''
        self.host = host
        self.port = port
        self.multicast = multicast
        print("Starting CoAP Server: " + host + ":" + str(port))
        print(self.root.dump())
        self.server = None
        #self.tempResourceHandler = TempResourceHandler()
        
    def start(self, timeout = 60):
        print("Starting CoAP Server: " + self.host + ":" + str(self.port))
        if self.server is None:
            self.server = CoAP((self.host, self.port), self.multicast)
        print(self.root.dump())
        try:
            self.server.listen(timeout)
        except KeyboardInterrupt:
            print("Server Shutdown")
            self.server.close()
            print("Exiting...")
            
    def stop(self):
        if self.server is None:
            print("No server is running")
        else:
            self.server.close()
            
    def addResource(self, path, resource):
        if self.server is None:
            print("No server is running")
        else:
            self.server.add_resource(path, resource)