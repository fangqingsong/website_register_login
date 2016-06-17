#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Content-Length': '688',
    'Content-Type':	'application/x-www-form-urlencoded',
    'Cookie': 'ASP.NET_SessionId=a3jsft45s140ld55arpf0545',
    'Host': 'vip.tdx.com.cn',
    'Referer': 'http://vip.tdx.com.cn/newindex/reg.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:42.0) Gecko/20100101 Firefox/42.0',
}

url = 'http://vip.tdx.com.cn/newindex/reg.aspx'

data = {
    'DropDownList1': '0',
    'TextBox3': 'welcome00',
    '__EVENTTARGET': 'LinkButton1',
    '__EVENTVALIDATION': '/wEWGQL687HGBQLJgJgBAsiAmAECpZywrAsC2pzcrAsC7NGKtQUCzPT7pg8C7NHufALs0YLYCQLs0fbZDALs0bLrBgKS++q2BALs0cbGDwLs0dqhCALs0f62CAKNi6WLBgLsr7jQCwKZgMS4CwLmpe3UBwLgj7/qAgLl7Z7BDgKXgrGaDwL+1OTXBQLs0ZKSAQKM54rGBiCQKzvmOl/MWP7Tnv7DhrSBptIt',
    '__VIEWSTATE': '/wEPDwULLTEzMzY2ODIzMzMPZBYCAgMPZBYEAgQPD2QWAh4Hb25jbGljawUQcmV0dXJuIGNoZWNrMigpO2QCEA8PZBYCHwAFEHJldHVybiBjaGVjazEoKTtkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQNqbjEFA2puMgUDam4y6dKS9azDcfItrP8/IRY7uGamb0Q=',
    'jn': '1',
    'jtype': 'gr',
}

res = requests.post(url, data=data, headers=headers)

if res.text.find(u'恭喜你可以使用！') != -1:
    print res.text.find(u'恭喜你可以使用！')
else:
    print 'hello world'
