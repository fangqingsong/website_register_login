#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'
from adsl import Adsl

import requests
import os
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
    'Cookie': 's=1t6312at61; xq_a_token=46e824dce44af699473d8786a8a16f2bdb33756c; xq_r_token=e4be0b883ba080bcb9dbf9138fcae5b7c6d84b98; _sid=LNkyLxcAtsrMB12WHNsAfh4PJHHUJK',
    'Host': 'xueqiu.com',
    'Referer': 'http://xueqiu.com/account/reg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'X-Requested-With': 'XMLHttpRequest',
}

url = 'http://xueqiu.com/account/sms/verify_telephone'

def write_file_positon(digit):
    with open('file_position.txt', 'w') as wf:
        wf.write(str(digit))

# 发送请求
def process_post_url(url, data, headers, line, position):
    try:
        res = requests.post(url, data=data, headers=headers)
        obj = res.json()
        if obj.has_key(u'message'):
            if not obj['success']:
                with open('result.txt', 'a') as f:
                    f.write(line)
            write_file_positon(position)
        elif obj.has_key(u'error_description') and obj['error_description'] == u'您注册过于频繁，请稍后再试':
            print u'您注册过于频繁，请稍后再试，需换ip...'
            # 重连adsl
            ad = Adsl()
            ad.reconnect()
            while True:
                # 判断网络是否通
                if sys.platform == 'win32':
                    ret = os.system('ping -n 2 www.baidu.com')
                else:
                    ret = os.system('ping -c 2 www.baidu.com')

                if not ret:
                    break
                else:
                    time.sleep(10)
        else:
            write_file_positon(position)
            sys.exit(0)
    except IOError:
        print 'network anomaly'
        time.sleep(5)
    except Exception:
        print 'url error'

def main():
    """
        验证号码，将注册后的号码保存到result.txt文件中
    """
    try:
        generate_phone_file = raw_input('Please input stored phone filename[hm.txt]: ')
        file_position = int(raw_input('Please enter a file index position[number]: '))
        with open(generate_phone_file, 'r') as rf:
            print('validate phone...')
            while True:
                line = rf.readline()
                current_file_position = rf.tell()
                if current_file_position >= file_position:
                    if not line: break
                    phone = line.strip()
                    print phone
                    data = {'telephone':phone, 'areacode':'86'}
                    process_post_url(url, data, headers, line, current_file_position)
        print 'Done!'
    except IOError:
        print 'No such file. Please input correct filename!'
    except ValueError:
        print 'Please input digit!'

if __name__ == '__main__':
    main()