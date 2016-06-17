#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

"""
	以下代码的含义是，将生成的自定义的号码段的号码保存到当前目录下的hm.txt文件中
"""

number = '1396532'

with open('hm.txt', 'w') as f:
	for i in range(0001, 10000):
		telephone = number + '{:0>4d}'.format(i) + '\n'
		f.write(telephone)
