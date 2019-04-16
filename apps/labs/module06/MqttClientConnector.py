'''
Created on Feb 19, 2019

CSYE 6530 -Connected Devices
@author: Doni Tampubolon
'''

import paho.mqtt.client as mqtt
import time

class MqttClientConnector(mqtt.Client):
    '''
    This class sets up and manages the connection between a client and a server(broker)
    All control packets are handled by an instance of this class
    '''
    def __init__(self,clientId=""):
        super().__init__(clientId)
        self.payload = None
        self.clientId = clientId
    
    '''
    This function is used to connect to the MQTT broker
    @param hostname: String url of broker
    @param port: int port number
    @param keepAlive: int time in seconds the connection is kept open
    '''      
    def connect(self, hostname="iot.eclipse.org", port=1883, keepAlive=60):
        self.hostname = hostname
        self.port = port
        
        print("Connecting to " + hostname)
        
        super().connect(hostname, port, keepAlive)
    
    '''
    This function is used to run the loop to ensure communication with the
    broker is carried out. It processes incoming and outgoing data.
    The loop must be kept running longer than the connection keepAlive time to make sure all packets from the broker are received
    i.e. runTime > keepAlive
    @param runTime: int the amount of time in seconds the loop is run
    '''
    def run(self, runTime=65):   
        '''
        rc = 0
        while rc ==0:
            rc = self.loop()
        '''
        
        self.loop_start()
        time.sleep(runTime)
        self.loop_stop()
        print("finish running")
        

    #Callback functions
    
    '''
    This function is called by Paho client when a successful connection with server(broker) is established
    client:     the client instance for this callback
    userdata:   the private user data as set in Client() or userdata_set()
    flags:      response flags sent by the broker
    rc:         the connection result (0 for successful)
    '''
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connection successful!\tReturned code: " + str(rc))
        else:
            print("Connection unsuccessful\tReturned code:" + rc)
    
    '''
    This function is called when the client disconnects form the server
    '''
    def on_disconnect(self, client, userdata, rc):
        if rc == 0:
            print("Succesfully disconnected from broker")
        else:
            print("Unexpected disconnection \tReturned code: " + rc)
        client.loop_stop()
    
    #This function is called when a subscriber client receives a publishes msg 
    def on_message(self, client, userdata, msg):
        print("Message Received: ")
        print("Topic: "+ msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        
        self.payload = msg.payload
    
    #This function is called when a message is published    
    def on_publish(self, client, userdata, mid):
        print("A message has been successfully published")
        print("mid " + str(mid))
    
    #This function is called when a new subscription is made    
    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscription successful..")
        print("Message id: " + str(mid) + "\tGranted QoS: " + str(granted_qos))
    
    #This function is called when the broker responds to an unsubscribe request.
    def on_unsubscribe(self, client, userdata, mid):
        print("Unsubscribed successfully")
        
    
    #This function is called when the client has log information for debugging
    #def on_log(self, client, userdata, level, buf):
    #    print(buf)
    