'''
Created on Apr 15, 2019

@author: Doni Tampubolon
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

from time import sleep
from project import PitchAdaptor
from project import TempSensAdapt
from labs.module06 import MqttClientConnector
from labs.common import DataUtil
from labs.common.PitchData import PitchData

#MQTT connection configuration:
pubTopic = "PitchData-CSYE6530"
pubTopic2 = "Temperature-CSYE6530"
payload = ""
name = "PitchSensor-CSYE6530"
connector = MqttClientConnector.MqttClientConnector(name)
dataUtil = DataUtil.DataUtil()
connector.connect("iot.eclipse.org", 1883)
connector.loop_start()

#pitch adaptor configuration
pitchAdaptor = PitchAdaptor.PitchAdaptor()
pitchAdaptor.daemon = True
pitchAdaptor.setEnable(True)
pitchAdaptor.start()
period = 10 #time interval in seconds to send reading to gateway
threshold = 310 #Minimum pitch in degrees that triggers app to send current reading to gateway


#temperature sensor adaptor configuration
tempSensorAdaptor = TempSensAdapt.TempSensorAdapt(connector)
tempSensorAdaptor.daemon = True
tempSensorAdaptor.setEnable(True)
tempSensorAdaptor.start()
maxTemp = 25

count=0

while(True):
    pitch = pitchAdaptor.getPitchData()
    curVal = pitch.getValue()
    print("Pitch: " + str(curVal))
    
    sensorData = tempSensorAdaptor.getSensorData()
    sensorVal = sensorData.getValue()
    
    if(curVal<=threshold and count%period!=0):
        #Sends MQTT message to alert the gateway device which is subscribed to the topic if the pitch is below the threshold
        print("ALERT: Pitch angle is below threshold")
        pd = PitchData()
        pd.setValue(curVal)
        payload = dataUtil.pitchDataToJson(pd)
        connector.publish(pubTopic, payload)

    elif count%10==0:
        #Sending new MQTT message every period of seconds if no threshold is exceeded 
        print("Constrained Device: Sending new pitch reading to gateway..")
        pd = PitchData()
        pd.setValue(curVal)
        payload = dataUtil.pitchDataToJson(pd)
        connector.publish(pubTopic, payload)
        
    if(sensorVal<=maxTemp and count%period!=0): 
        #Sending new MQTT message every period of seconds if no threshold is exceeded 
        print("Constrained Device: Sending new temperature reading to gateway..")
        payload2 = dataUtil.sensorDataToJson(sensorData)
        connector.publish(pubTopic2, payload2)
        
    count+=1
    sleep(1)
    
def updateTemperature(newVal):
    return newVal