'''
Created on Feb 19, 2019

CSYE 6530 -Connected Devices
@author: Doni Tampubolon
'''

import paho.mqtt.client as mqtt
import os

class MqttClientConnector():
    '''
    This class sets up and manages the connection between a client and a server(broker)
    All control packets are handled by an instance of this class
    '''

    def __init__(self, client_id="", hostname="test.mosquitto.org", port=1883):
        '''
        Constructor
        '''
        self.client_id = client_id
        self.hostname = hostname
        self.port = port
        
        self.client = mqtt.Client(client_id)
        
        #Event callback assignments
        self.client.on_connect = on_connect
        self.client.on_disconnect = on_disconnect
        self.client.on_message = on_message
        self.client.on_publish = on_publish
        self.client.on_subscribe = on_subscribe
        #self.client.on_log = on_log
            
    def start(self):
        print("Starting loop..")
        self.client.loop_start()
            
    def connect(self):
        print("Connecting to broker: " + str(self.hostname))
        self.client.connect(self.hostname,self.port)
    
    def disconnect(self):
        print("Disconnecting from broker: " + str(self.hostname))
        self.client.disconnect()
        
    def publish(self, topic, message):
        print("Publishing message..")
        self.client.publish(topic, message)
        
    def subscribe(self, topic, qos):   
        print("Subscribing to topic: " + topic)
        self.client.subscribe(topic, qos)
        
    def unsubscribe(self, topic):
        print("Unsubscribing from topic: " + topic)
        self.client.unsubscribe(topic)
        
#Callback functions

'''
This function is called by Paho client when a successful connection with server(broker) is established
client:     the client instance for this callback
userdata:   the private user data as set in Client() or userdata_set()
flags:      response flags sent by the broker
rc:         the connection result (0 for successful)
'''
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection successful!\tReturned code: " + rc)
    else:
        print("Connection unsuccessful\tReturned code:" + rc)

'''
This function is called when the client disconnects form the server
'''
def on_disconnect(client, userdata, rc):
    if rc == 0:
        print("Succesfully disconnected from broker")
    else:
        print("Unexpected disconnection \tReturned code: " + rc)
    client.loop_stop()

#This function is called when a subscriber client receives a publishes msg 
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

#This function is called when a message is published    
def on_publish(client, userdata, mid):
    print("A message has been successfully published")
    print("mid " + str(mid))

#This function is called when a new subscription is made    
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscription successful..")
    print("Message id: " + str(mid) + "\tGranted QoS: " + str(granted_qos))

#This function is called when unsubscription is done
def on_unsubscribe(client, userdata, mid):
    print("Unsubscribed successfully")

#This function is called when the client has log information for debugging
def on_log(client, userdata, level, buf):
    print(buf)