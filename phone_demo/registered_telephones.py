#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests

"""
    http://www.jrj.com.cn/
"""

headers = {
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Host': 'sso.jrj.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://sso.jrj.com.cn/sso/passportRegister/register.jsp?SysID=&ReturnURL=&fromId=&from=&tgqdcode=3763BEXX',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:41.0) Gecko/20100101 Firefox/41.0',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'https://sso.jrj.com.cn/sso/ajaxValidateUser'

def create_db_if_need():
    """
    如果不存在数据表则创建，数据表用来保存已运行过的号码
    """
    from sqlite_db import conn
    c = conn.cursor()
    create_table_sql = 'CREATE TABLE IF NOT EXISTS telephones (phone text)'
    c.execute(create_table_sql)
    conn.commit()

def get_all_phones():
    """
    获取已经运行过的号码,用于过滤
    """
    from sqlite_db import conn
    c = conn.cursor()
    phones = list(c.execute('SELECT phone FROM telephones'))
    return phones


def main():
    """
        从输入的文件hm.txt中获取号码一一验证，将已经注册的号码保存到resutl.txt文件中
    """
    create_db_if_need()
    phones_already = get_all_phones()

    generate_phone_file = raw_input('Please input phone filename: ')

    from sqlite_db import conn
    c = conn.cursor()

    try:
        with open(generate_phone_file, 'r') as f:
            print('validate phone...')
            while True:
                line = f.readline()
                if not line: break
                phone = line.strip()
                if (phone,) in phones_already: continue
                data = {'userName': phone}
                try:
                    # 以post的方式发送请求
                    res = requests.post(url, data=data, headers=headers)
                    result_value = res.json()['result']

                    if result_value == 'userExist':
                        # 将已经注册的号码保存到当前目录下的result.txt文件中，注意此处是以追加的方式写入数据
                        with open('result.txt', 'a') as rf:
                            rf.write(line)

                except Exception as e:
                    print str(e)

                c.execute('INSERT INTO telephones VALUES (' + phone + ')')
                conn.commit()
        print 'Done!'

    except IOError:
        print 'No such file. Please input correct filename!'

    finally:
        # 关闭打开的链接
        c.close()
        conn.close()

if __name__ == '__main__':
    main()
