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

def get_connect():
    """
        获取sqlite3的链接
    """
    import sqlite3
    return sqlite3.connect('tdx.db')

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
                data = {
                    'DropDownList1': '0',
                    'TextBox3': phone,
                    '__EVENTTARGET': 'LinkButton1',
                    '__EVENTVALIDATION': '/wEWGQL687HGBQLJgJgBAsiAmAECpZywrAsC2pzcrAsC7NGKtQUCzPT7pg8C7NHufALs0YLYCQLs0fbZDALs0bLrBgKS++q2BALs0cbGDwLs0dqhCALs0f62CAKNi6WLBgLsr7jQCwKZgMS4CwLmpe3UBwLgj7/qAgLl7Z7BDgKXgrGaDwL+1OTXBQLs0ZKSAQKM54rGBiCQKzvmOl/MWP7Tnv7DhrSBptIt',
                    '__VIEWSTATE': '/wEPDwULLTEzMzY2ODIzMzMPZBYCAgMPZBYEAgQPD2QWAh4Hb25jbGljawUQcmV0dXJuIGNoZWNrMigpO2QCEA8PZBYCHwAFEHJldHVybiBjaGVjazEoKTtkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQNqbjEFA2puMgUDam4y6dKS9azDcfItrP8/IRY7uGamb0Q=',
                    'jn': '1',
                    'jtype': 'gr',
                }
                try:
                    res = requests.post(url, data=data, headers=headers)
                    if res.text.find(u'帐号已存在！') != -1:
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