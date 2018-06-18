#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

line = '1000以上	15'

print(line.split('\t')[0][len(line.split('\t')[0]) - 1] == '上')