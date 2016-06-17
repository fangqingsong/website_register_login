#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests
import json

headers = {
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Host': 'sso.jrj.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://sso.jrj.com.cn/sso/passportRegister/register.jsp?SysID=&ReturnURL=&fromId=&from=&tgqdcode=3763BEXX',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:41.0) Gecko/20100101 Firefox/41.0',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'https://sso.jrj.com.cn/sso/ajaxValidateUser'
data = {'userName': '18693085370'}
res = requests.post(url, data=data, headers=headers)
print res.json()['result']
