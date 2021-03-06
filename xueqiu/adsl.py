# -*- coding: utf-8 -*-
import os
import time

"""
    需要为特定的宽带账号创建一个新的宽带连接，填上相应的isp名称、用户名、密码
"""

g_adsl_account = {"name": "adsl",
                "username": "057112548856",
                "password": "572641"}
     
class Adsl(object):
    #==============================================================================
    # __init__ : name: adsl名称
    #==============================================================================
    def __init__(self):
        self.name = g_adsl_account["name"]
        self.username = g_adsl_account["username"]
        self.password = g_adsl_account["password"]
 
         
    #==============================================================================
    # set_adsl : 修改adsl设置
    #==============================================================================
    def set_adsl(self, account):
        self.name = account["name"]
        self.username = account["username"]
        self.password = account["password"]
 

    #==============================================================================
    # connect : 宽带拨号
    #==============================================================================
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        os.system(cmd_str)
        time.sleep(5)
 

    #==============================================================================
    # disconnect : 断开宽带连接
    #==============================================================================
    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        time.sleep(5)
 
     
    #==============================================================================
    # reconnect : 重新进行拨号
    #==============================================================================
    def reconnect(self):
        self.disconnect()
        self.connect()