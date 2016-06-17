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
                print 'checking: ', phone
                try:
                    res = requests.get(url.format(phone), headers=headers)
                    if res.json()['data'] == 1:
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