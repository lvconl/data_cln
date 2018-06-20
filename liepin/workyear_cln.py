#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import re

filt = re.compile('\n')

f = open('../liepin/workyear_data/workyear.txt')

def load_data():
    '''
    加载从hive导出的原始数据，以及过滤不相关数据
    :return: work_list
    '''
    line = f.readline()
    work_list = []
    while line:
        tmp = line.strip().split('\t')
        work_list.append(tmp)
        line = f.readline()
    return work_list

def save_to_csv():
    work_list = load_data()
    work_df = pd.DataFrame(work_list)
    work_df.columns = ['work','count']
    work_df.to_csv('../liepin/workyear_data/raw_work.csv',index=None)
    print('转存csv成功')

def run_main_liepin():
    save_to_csv()

if __name__ == '__main__':
    save_to_csv()