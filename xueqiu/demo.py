#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests
import sys
import time

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'Keep-Alive',
    'Content-Length': '33',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 's=2zj212cccy; xq_a_token=623394d80ef89b484bbb46ff591adc135b37850b; xq_r_token=75847f139872b45471ea9ab2b28a62f75a98dd7e; _sid=D5dJ0hB6M3Kb36kshDZPK1b5W4iRMR',
    'Host': 'xueqiu.com',
    'Referer': 'http://xueqiu.com/account/reg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'X-Requested-With': 'XMLHttpRequest',
}

# headers = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Connection': 'keep-alive',
#     'Content-Length': '33',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie': 's=2wqj12n0b5; xq_a_token=9d5c52db5d031594dc48856217192de364e69877; xq_r_token=40e47afe96856915b0033e0beded4c340d3ffdb7; _sid=YJAEV7zZCokeEGdSbrPkrJ8vcYWWKZ',
#     'Host': 'xueqiu.com',
#     'Origin': 'http://xueqiu.com',
#     'Referer': 'http://xueqiu.com/account/reg',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
# }

url = 'http://xueqiu.com/account/sms/verify_telephone'
data = {'telephone':'18693085370', 'areacode':'86'}

# def process_post_url(url, data, headers, line, position):
#     try:
#         res = requests.post(url, data=data, headers=headers)
#         obj = res.json()
#         if obj.has_key(u'message'):
#             if not obj['success']:
#                 with open('result.txt', 'a') as f:
#                     f.write(line)
#         else:
#             sys.exit(0)
#     except IOError:
#         print 'network anomaly'
#         time.sleep(5)
#     except Exception:
#         print 'url error'

try:
    res = requests.post(url, data=data, headers=headers)
    obj = res.json()
    if obj.has_key(u'error_description') and obj['error_description'] == u'您注册过于频繁，请稍后再试':
        print obj['error_description']
    print res.text
    # print res.text
    #
    # if res.json().has_key(u'message'):
    #     print 'OK'
    # if res.json().has_key(u'error_code'):
    #     print 'error_code'

    if not res.json()['success']:
        print 'hello', res.text, res.json()['success']
except Exception as e:
    print e


# # return语句直接退出函数，不管这个return语句是否被for或者是while循环包裹。
# def demo(number):
#     while True:
#         number += 1
#         if number >= 10: return
#         print number
#     print 'hello world'
#
# demo(1)

# try:
#     res = requests.post(url, data=data, headers=headers)
#     if not res.json()['success']:
#         with open('result.txt', 'a') as f:
#             f.write('18693085370')
# except TypeError:
#     with open('file_position.txt', 'a') as wf:
#         wf.write('23')
#     print 'error'
#     sys.exit()

# res = requests.post(url, data=data, headers=headers)
# obj = res.json()
# if obj.has_key(u'message'):
#     if not obj['success']:
#         with open('result.txt', 'a') as f:
#             f.write('18693085370')
# else:
#     with open('file_position.txt', 'w') as wf:
#         wf.write('23')
#     print 'hello world'
#     sys.exit(0)


# if not res.json()['success']:
#     print res.text, res.json()['success']

# i = 0
# while True:
#     if i == 5: sys.exit(0)
#     res = requests.post(url, data=data, headers=headers)
#     print res.text, i
#     i += 1

# while True:
#     with open('hm.txt', 'r') as rf:
#         line = rf.readline()
#         if not line: break
#         print line
#         a = rf.readlines()
#         print a[1:]

# with open('hm.txt', 'r') as rf:
#     while True:
#         line = rf.readline()
#         current_file_position = rf.tell()
#         if current_file_position < 36205: continue
#         if not line: break
#         print line