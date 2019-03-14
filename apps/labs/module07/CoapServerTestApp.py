'''
Created on Mar 7, 2019

@author: Doni Tampubolon
'''
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
from labs.module07.CoapServerConnector import CoapServerConnector

class CoapServerTestApp():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.connector = CoapServerConnector()
        
if __name__ == '__main__':
    #Creating Server App instance
    serverApp = CoapServerTestApp()
    serverApp.connector.start(6000)
    