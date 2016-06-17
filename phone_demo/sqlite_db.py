#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import sqlite3


"""
    此处，使用python内置的sqlite3数据库
    1. 连接到sqlite3数据库
    2. 数据库文件是data.db
    3. 如果文件不存在，则会在当前目录创建
"""

conn = sqlite3.connect('data.db')
