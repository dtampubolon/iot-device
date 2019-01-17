#Lab module 1
#CSYE6530 - Connected Devices
#Doni Tampubolon - NUID 001400708

from time import sleep
from labs.module01 import SystemPerformanceAdaptor

SPA = SystemPerformanceAdaptor.SystemPerfromanceAdaptor(1,"SPA-1", 8) #Create SystemPerformanceAdaptor instance
SPA.daemon = True #Runs thread as a background task

print("System performance app is starting as a daemon thread..")
SPA.setEnable(True) #Enable SystemPerformanceAdaptor instance
SPA.start() #Start SPA thread

while (True): #Allow main thread to run indefinitely 
    sleep(1)
    pass
