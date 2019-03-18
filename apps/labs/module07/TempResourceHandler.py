'''
Created on Mar 7, 2019

@author: Doni Tampubolon
'''
import time
from coapthon import defines
from coapthon.resources.resource import Resource

class TempResourceHandler(Resource):
    '''
    This class is a resource handler for CoAP servers
    '''
    def __init__(self, name = "TempResourceHandler", coap_server = None):
        '''
        Constructor
        '''
        super().__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.payload = ""
        self.resource_type = "JSON"
        self.content_type = "text/plain"
        #self.interface_type = "if1"
    
    '''
    This function is called when a GET request is received
    '''
    def render_GET(self, request):
        return self
    
    '''
    This function is called when a PUT request is received
    '''
    def render_PUT(self, request):
        self.edit_resource(request)
        return self
    
    '''
    This function is called when a POST request is received
    '''    
    def render_POST(self, request):
        res = self.init_resource(request, TempResourceHandler())
        return res
    
    '''
    This function is called when a DELETE request is received
    '''
    def render_DELETE(self, request):
        return True
    