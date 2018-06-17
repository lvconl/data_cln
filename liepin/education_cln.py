#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import re


filt = re.compile('\n')
f = open('./education_data/education.txt')


def load_data_from_txt():
    '''
    从txt文件中加载原始数据
    :return:
    '''
    line = f.readline()
    edu_list = []
    while line:
        tmp = line.split('\t')
        tmp[1] = filt.sub(r'',tmp[1])
        edu_list.append(tmp)
        line = f.readline()
    return edu_list

def save_to_csv():
    edu_list = load_data_from_txt()
    edu_df = pd.DataFrame(edu_list)
    edu_df.columns = ['edu','count']
    edu_df.to_csv('./education_data/raw_edu.csv',index=None)
    print('转存csv成功')

if __name__ == '__main__':
    save_to_csv()