'''
Created on Apr 15, 2019

@author: Doni Tampubolon
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

from time import sleep
from project import PitchAdaptor
from labs.module06 import MqttClientConnector
from labs.common import DataUtil

#pitch adaptor configuration
pitchAdaptor = PitchAdaptor.PitchAdaptor()
pitchAdaptor.daemon = True
pitchAdaptor.setEnable(True)
pitchAdaptor.start()
period = 30 #time interval in seconds to send reading to gateway
threshold = 310 #Minimum pitch in degrees that triggers app to send current reading to gateway

#MQTT connection configuration:
topic = "PitchData-CSYE6530"
payload = ""
name = "PitchSensor-CSYE6530"
connector = MqttClientConnector.MqttClientConnector(name)
dataUtil = DataUtil.DataUtil()
connector.connect("iot.eclipse.org", 1883)
connector.loop_start()

while(True):
    pitch = pitchAdaptor.getPitchData()
    curVal = pitch.getValue()
    print(curVal)
    if(curVal<=threshold):
        #Sends MQTT message to alert the gateway device which is subscribed to the topic if the pitch is below the threshold
        print("WARNING: current pitch is below threshold, sending alert to gateway\n")
        payload = dataUtil.pitchDataToJson(pitch)
        connector.publish(topic, payload)
    else:
        sleep(1)
    