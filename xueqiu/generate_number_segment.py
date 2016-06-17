#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    1820170,21,上海
    1820171,21,上海
    1820172,21,上海
    1820173,21,上海
    ...
    上面格式的号码字符串存储在mobile_number_section.txt文件中，获取到的号段写入
    number_segment.txt文件中。文件number_segment.txt中可以有原始数据。
"""
with open(u'全国号段地区文件.txt', 'r') as rf:
    while True:
        line = rf.readline()
        if not line: break
        with open('number_segment.txt', 'a') as f:
            f.write('\n' + line.strip().split(',')[0])