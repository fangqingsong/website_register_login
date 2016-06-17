#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests
import datetime
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=1A208AB60C6C6FA41B50FB4BBC45C9D2',
    'Host': 'www.gsshy.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:42.0) Gecko/20100101 Firefox/42.0',
}

url = 'http://www.gsshy.org/'

while True:
    time.sleep(10)
    res = requests.get(url, headers=headers)

    if res.text.find(u'习近平') == -1:
        with open('result.txt', 'a') as rf:
            rf.write(str(datetime.datetime.now()) + '\n')
        print 'not stable'
    else:
        print datetime.datetime.now()