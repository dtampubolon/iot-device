'''
Created on Jan 19, 2019

@author: Doni Tampubolon
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

import smtplib
from labs.common import ConfigUtil
from labs.common import ConfigConst
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SmtpClientConnector():
    '''
    This class creates a connection to SMTP server and 
    send messages through said server
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.config = ConfigUtil.ConfigUtil(r'C:\Users\Doni Tampubolon\Documents\Grad School\CSYE6530\gitrepo\iot-device\apps\labs\data\ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))

        
    def publishMessage(self, topic, data):
        host = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        
        msg.attach(MIMEText(msgBody))
        msgText = msg.as_string()
        # send e-mail notification
        
        smtpServer = smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
