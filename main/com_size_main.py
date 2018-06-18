#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd

from liepin.com_size_cln import run_main_liepin
from qcwy.com_size_cln import run_main_qcwy

def load_data():
    '''
    从各个网站的文件夹中加载原始数据
    :return: toget_df
    '''
    qcwy_df = pd.read_csv('../qcwy/com_size_data/raw_com_size.csv')
    liepin_df = pd.read_csv('../liepin/com_size_data/raw_com_size.csv')
    toget_df = pd.concat([qcwy_df,liepin_df],axis=0,ignore_index=True)
    toget_df['count'] = toget_df['count'].apply(int)
    return toget_df

def size_static():
    data_df = load_data()
    less_hundred = data_df[(data_df['size'] == '1-49人') | (data_df['size'] == '50-99人') | (data_df['size'] == '50-150人')]['count']
    print('少于100人:{}'.format(sum(less_hundred.values.tolist())))
    hundred_five_hundred = data_df[(data_df['size'] == '150-500人') | (data_df['size'] == '100-499人')]['count']
    print('100-500人:{}'.format(sum(hundred_five_hundred.values.tolist())))
    five_hundred_thousands = data_df[(data_df['size'] == '500-999人') | (data_df['size'] == '500-1000人')]['count']
    print('500-1000人:{}'.format(sum(five_hundred_thousands.values.tolist())))
    thousands_five_thousands = data_df[(data_df['size'] == '1000-5000人') | (data_df['size'] == '1000-2000人') | (data_df['size'] == '2000-5000人')]['count']
    print('1000-5000人:{}'.format(sum(thousands_five_thousands.values.tolist())))
    five_thousands_one_lion = data_df[(data_df['size'] == '5000-10000人')]['count']
    print('5000-10000人:{}'.format(sum(five_thousands_one_lion.values.tolist())))
    more_lion = data_df[data_df['size'] == '10000人以上']['count']
    print('10000以上:{}'.format(sum(more_lion.values.tolist())))

if __name__ == '__main__':
    run_main_liepin()
    run_main_qcwy()
    size_static()