#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '33',
    'Content-Type':	'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 's=1r5f1b8b9q; xq_a_token=3fb8ee46a1428ecd37fb311807023ff326fb2805; xq_r_token=3166da8de72ec09d890dd9bd0ce37d6e3da0271a',
    'Host': 'xueqiu.com',
    'Referer': 'http://xueqiu.com/account/reg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://xueqiu.com/account/sms/verify_telephone'

def get_connect():
    """
        获取sqlite3的链接
    """
    import sqlite3
    return sqlite3.connect('xueqiu.db')

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
    generate_phone_file = raw_input('Please input stored phone filename: ')
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
                print 'checking: ', phone
                data = {'telephone':phone, 'areacode':'86'}
                try:
                    res = requests.post(url, data=data, headers=headers)
                    if not res.json()['success']:
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