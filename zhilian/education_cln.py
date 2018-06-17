#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import re

f = open('./education_data/education.txt')
filt = re.compile('\n')

def filt_data():
    '''
    过滤非学历脏数据
    :return: edu_list
    '''
    edu_list = []
    line = f.readline()
    while line:
        if line[:2] == '学历':
            edu_tmp = []
            tmp = line.split('\t')
            edu = tmp[0][3:len(tmp[0])]
            if not edu is '':
                count = filt.sub(r'',tmp[1])
                edu_tmp.append(edu)
                edu_tmp.append(count)
                edu_list.append(edu_tmp)
        line = f.readline()
    return edu_list

def save_to_csv():
    edu_list = filt_data()
    edu_df = pd.DataFrame(edu_list)
    edu_df.columns = ['edu','count']
    edu_df.to_csv('./education_data/raw_edu.csv',index=None)
    print('转存csv成功')

if __name__ == '__main__':
    save_to_csv()