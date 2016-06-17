#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests
from random import randint

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '17',
    'Content-Type':	'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'Hm_lvt_d25bd1db5bca2537d34deae7edca67d3=1448382549;Hm_lpvt_d25bd1db5bca2537d34deae7edca67d3=1448382788;lzstat_uv=28992565033010800607|884719;lzstat_ss=2434049949_2_1448411588_884719;pgv_pvi=6909144064;pgv_si=s8494584832;800078599slid=slid_25_6%7C;800078599mid=40_44;800078599mh=1448382763815;800078599slid_25_6=1448382763817;chart_userid=b90d1e7b-b871-4103-97f7-4ad74e356c73;chart_username=hello_zz;ASP.NET_SessionId=wlx20o1k4txcitj4izhdfcev',
    'Host': 'auth.fx678.com',
    'Pragma': 'no-cache',
    'Referer': 'http://auth.fx678.com/OAuth/Register?oauth_method=member&oauth_account=member&oauth_signature=c7764cfed23c5ca3bb393308a0da2306&oauth_timespan=1448411520.14215&oauth_callback=http://t.fx678.com/index/livetrade/RegisterHandler.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:42.0) Gecko/20100101 Firefox/42.0',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://auth.fx678.com/Share/CheckPhone?clientid=Phone&rand={0}&Account=&Phone={1}'

def get_connect():
    """
        获取sqlite3的链接
    """
    import sqlite3
    return sqlite3.connect('fx678.db')

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
                data = {'phone':phone}
                try:
                    res = requests.post(url.format('144838'+str(randint(1000000, 9999999)), phone), data=data, headers=headers)
                    if res.text == '1':
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