#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import numpy as np
import re

f = open('./education_data/education.txt')
file = re.compile('\n')

def edu_to_list():
    '''
    读取原始数据，过滤非学历数据，返回与学历相关数据
    :return:edu_list
    '''
    edu_list = []
    line = f.readline()
    while line:
        if line[0] != '招' and line[0] != 'N':
            line = file.sub('',line)
            edu_list.append(line)
        line = f.readline()
    return edu_list

def split_edu_count(edu_list):
    '''
    将学历及其数目分割
    :return:
    '''
    result_list = []
    for item in edu_list:
        tmp = item.split('\t')
        result_list.append(tmp)
    return result_list

def run_main():
    edu_list = edu_to_list()
    split_list = split_edu_count(edu_list)
    edu_df = pd.DataFrame(split_list)
    edu_df.columns = ['edu','count']
    edu_df.to_csv('./education_data/raw_edu.csv',index=None)
    print('转存csv成功')


if __name__ == '__main__':
    run_main()