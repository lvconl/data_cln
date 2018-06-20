#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd

f = open('../qcwy/workyear_data/workyear.txt')


def load_data():
    '''
    加载原始数据
    :return: work_list
    '''
    line = f.readline()
    work_list = []
    while line:
        tmp = line.strip().split('\t')
        if not tmp[0] == 'NULL':
            work_list.append(tmp)
        line = f.readline()
    return work_list

def sava_to_csv():
    work_list = load_data()
    work_df = pd.DataFrame(work_list)
    work_df.columns = ['work','count']
    work_df.to_csv('../qcwy/workyear_data/raw_work.csv',index=None)
    print('转存csv成功')

def run_main_qcwy():
    sava_to_csv()

if __name__ == '__main__':
    sava_to_csv()