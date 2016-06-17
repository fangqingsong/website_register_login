#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '29',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'Hm_lvt_f9ca5b72be89420e57d2096db667c2a4=1449029255',
    'Host': 'www.niuguwang.com',
    'Origin': 'http://www.niuguwang.com',
    'Referer': 'http://www.niuguwang.com/index/views/user-reg.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://www.niuguwang.com/user/webapi/checkmobile.ashx'

def get_connect():
    """
        获取sqlite3的链接
    """
    import sqlite3
    return sqlite3.connect('niuguwang.db')

def get_phones_from_db():
    """
        获取到保存在数据库表中的号码
    """
    conn = get_connect()
    cursor = conn.cursor()
    phones = []
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS telephones (phone text)')
        phones = list(cursor.execute('SELECT phone FROM telephones'))
        conn.commit()
    except Exception as e:
        print str(e)
    finally:
        cursor.close()
        conn.close()
    return phones

def main():
    """
        验证号码，将注册后的号码保存到特定的文件中
    """
    phones_already = get_phones_from_db()
    generate_phone_file = raw_input('Please input stored phone filename [hm.txt]: ')
    conn = get_connect()
    cursor = conn.cursor()
    try:
        with open(generate_phone_file, 'r') as f:
            print('validate phone...')
            while True:
                line = f.readline()
                if not line: break
                phone = line.strip()
                if (phone,) in phones_already: continue
                print 'checking:', phone
                data = {'packtype':'9', 'mobile':phone}
                try:
                    res = requests.post(url, data=data, headers=headers)
                    if res.json()['message'] == u'手机号码已存在':
                        with open('result.txt', 'a') as rf:
                            rf.write(line)
                except Exception as e:
                    print str(e)
                cursor.execute('INSERT INTO telephones VALUES (' + phone + ')')
                conn.commit()
        print 'Done!'
    except IOError:
        print 'No such file. Please input correct filename!'
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()