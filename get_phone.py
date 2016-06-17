# -*- coding: utf-8 -*-

import requests
import time
import random
import os
import sys

from adsl import Adsl

url = 'http://i.10jqka.com.cn/ucenter/register/isPhoneCanBeBindedNew'
# url = 'http://i.10jqka.com.cn/ucenter/register/isPhoneCanBeBinded'
headers = {
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,ko;q=0.2,zh-TW;q=0.2',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '17',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'i.10jqka.com.cn',
    'Origin': 'http://i.10jqka.com.cn',
    'Pragma': 'no-cache',
    'RA-Sid': '3A65D2DE-20140808-051402-1053d8-0c4bf5',
    'RA-Ver': '2.10.4',
    'Referer': 'http://i.10jqka.com.cn/ucenter/register/triggering/MXEydzNlNHI1dHEKMTIzNDU2CjE1OTkwMDQ0NjYxCnFxQHFxLmNvbQowMDEwNDgK',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
    'PHPSESSID': '9vl4icugipp4pcoo5o8g9bisk3',
    'user': 'MDoxcTJ3M2U0cjV0cTplMTBhZGMzOTQ5YmE1OWFiYmU1NmUwNTdmMjBmODgzZTpOb25lOjUwMDoyODAwMjY2Mzk6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOjo6OjI3MDAyNjYzOToxNDM0NTE5NDE0Ojo6MTQzNDUxOTM2MA%3D%3D',
    'userid': '270026639',
    'u_name': '1q2w3e4r5tq',
    'escapename': '1q2w3e4r5tq',
    'ticket': 'b9f3e348df15d560c7626cf0af86c060',
    '__utmt': '1',
    '__utma': '89518403.308567809.1434519417.1434519417.1434519417.1',
    '__utmb': '89518403.2.10.1434519417',
    '__utmc': '89518403',
    '__utmz': '89518403.1434519417.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}


# def get_ips():
#     """ 获取代理IP """
#     proxy_api = 'http://evxr.daili666.com/ip/?tid=558584997408640&num=10&ports=80'
#     ips = requests.get(proxy_api).content.split('\r\n')
#     return ips


# def make_proxies(ip):
#     """ 构建代理 """
#     return {'http': 'http://'+ip}


def init_db_if_need():
    """
    如果不存在数据表则创建
    """
    from sqlite_db import conn
    c = conn.cursor()
    create_table_sql = "CREATE TABLE IF NOT EXISTS numbers (phone text)"
    c.execute(create_table_sql)
    conn.commit()
    # conn.close()



def get_all_numbers():
    """
    获取已经运行过的号码,用于过滤
    """
    from sqlite_db import conn
    c = conn.cursor()
    phones = list(c.execute("SELECT phone FROM numbers"))
    print phones
    # conn.close()
    return phones



def main():
    # 如果不存在存放电话号码的数据表，则创建一个
    init_db_if_need()
    phones_already = get_all_numbers()

    filename = raw_input('Please input filename: ')
    from sqlite_db import conn

    c = conn.cursor()

    count = 0
    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line: break
                phone = line.strip()

                if phone in phones_already:
                    print 'pass'
                    continue

                payload = {'phone': phone}

                try:
                    res = requests.post(url, headers=headers, data=payload)
                    count += 1
                    err_code = res.json()['errorcode']
                    print res.json()

                    if err_code != 0:
                        with open('result.txt', 'a') as rf:
                            rf.write(line)

                    if count % 3 == 0:
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

                except Exception, e:
                    print str(e)

                c.execute("INSERT INTO numbers VALUES (" + phone + ")")
                conn.commit()
        conn.close()
        print 'Done!'

    except IOError:
        print 'No such file.Please run it agian!'

if __name__ == '__main__':
    main()
