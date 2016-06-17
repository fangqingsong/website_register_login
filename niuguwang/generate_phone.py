#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Administrator'

# 打开已经存在的且保存号段的文件 number_segment.txt，将里面的每一个号段都生成需要的号码
with open('number_segment.txt', 'r') as rf:
    while True:
        line = rf.readline()
        if not line: break
        number_segment = line.strip()
        with open('hm.txt', 'a') as f:
            for i in range(0001, 10000):
                if number_segment:
                    telephone = number_segment + '{:0>4d}'.format(i) + '\n'
                    f.write(telephone)