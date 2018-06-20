#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd

f = open('../zhilian/workyear_data/workyear.txt')

def load_data():
    '''
    加载并过滤从hive中导出的原始数据
    :return: work_list
    '''
    line = f.readline()
    work_list = []
    while line:
        if line[0:2] == '经验':
            tmp = line.strip().split('\t')
            tmp[0] = tmp[0][3:len(tmp[0])]
            work_list.append(tmp)
        line = f.readline()
    return work_list


def save_to_csv():
    work_list = load_data()
    work_df = pd.DataFrame(work_list)
    work_df.columns = ['work','count']
    work_df.to_csv('../zhilian/workyear_data/raw_work.csv',index=None)
    print('转存csv成功')

def run_main_zhilian():
    save_to_csv()

if __name__ == '__main__':
    save_to_csv()