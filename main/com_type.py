#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import jieba
from collections import Counter

jieba.enable_parallel(4)

f = open('../main/com_type_data/out.txt','r')

context = f.read()

words = jieba.cut(context)

count = Counter(words).most_common(10)

for item in count:
    print('{}:{}'.format(item[0],item[1]))