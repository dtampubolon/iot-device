#Lab module 1
#CSYE6530 - Connected Devices
#Doni Tampubolon - NUID 001400708
import psutil
import threading
import time

class SystemPerfromanceAdaptor(threading.Thread):
    #Constructor
    def __init__(self, threadID, name, period):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.period = period #Wake up every period of seconds
        self.enable = False
        
    #When thread is started, this method is called
    def run(self):
        while True:
            if  self.enable:
                print("\n---------")
                print("System performance readings at: " + time.ctime())
                print("CPU: " + str(psutil.cpu_times()))
                print("Memory: " + str(psutil.virtual_memory()))
            time.sleep(self.period)
    
    #This method is used to enable the performance adaptor
    def setEnable(self, enable):
        self.enable = enable