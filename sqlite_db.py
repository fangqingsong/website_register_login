# -*- coding: utf-8 -*-

import sqlite3

# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('record.db')
