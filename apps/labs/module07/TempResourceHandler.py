'''
Created on Mar 7, 2019

@author: Doni Tampubolon
'''
import time
from coapthon import defines
from coapthon.resources.resource import Resource

class TempResourceHandler(Resource):
    '''
    classdocs
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

    def render_GET(self, request):
        return self
    
    def render_PUT(self, request):
        self.edit_resource(request)
        return self
        
    def render_POST(self, request):
        res = self.init_resource(request, TempResourceHandler)
        return res
    
    def render_DELETE(self, request):
        return True
    