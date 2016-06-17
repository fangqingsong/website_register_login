#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests

headers = {
    'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cookie': 'CNZZDATA30040885=cnzz_eid%3D288531303-1448871981-http%253A%252F%252Fwww.huagu.com%252F%26ntime%3D1448883725; CNZZDATA30041999=cnzz_eid%3D1009972480-1448871981-http%253A%252F%252Fwww.huagu.com%252F%26ntime%3D1448883725; CNZZDATA30054472=cnzz_eid%3D1757150657-1448872085-http%253A%252F%252Fsns.huagu.com%252F%26ntime%3D1448872085; 412720c552eae1a8577343ae5bac8499=1; PHPSESSID=d7f1a2050c53f99276f9ab6c47ab1c1a',
    'Host': 'sns.huagu.com',
    'Referer': 'http://sns.huagu.com/register.php?reurl=http://www.huagu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:42.0) Gecko/20100101 Firefox/42.0',
    'X-Prototype-Version': '1.7',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://sns.huagu.com/reg/status.php?account={0}'

res = requests.get(url.format('18693085379'), headers=headers)

if res.json()['data'] == 1:
    print 'OK'
print res.text, res.json()['data']
