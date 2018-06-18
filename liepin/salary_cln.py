#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd

data = pd.read_csv('../liepin/data/raw_salary.csv')
def rang_to_avg(salary_rang_str):
    '''
    将给出的工资范围计算出平均数
    :param rang: 工资范围
    :return: 工资范围的平均数
    '''
    salary_str = salary_rang_str[:len(salary_rang_str) - 1]
    max_min_list = salary_str.split('-')
    min_value = int(max_min_list[0])
    max_value = int(max_min_list[1])
    avg = float(min_value + max_value) * 10000 / 24
    return avg
def run_main_liepin():
    save_to_csv()
    salary_df = pd.DataFrame(data)
    salary_df['rang'] = salary_df['rang'].apply(rang_to_avg)
    salary_df.to_csv('../liepin/data/cln_data/cln_salary.csv',index=None)
    print('转存csv成功')

def save_to_csv():
    f = open('../liepin/data/salary.txt')
    line = f.readline()
    data_list = []
    while line:
        if not line[0] == '面':
            tmp = line.strip().split('\t')
            data_list.append(tmp)
        line = f.readline()
    data_df = pd.DataFrame(data_list)
    data_df.columns = ['rang','count']
    data_df.to_csv('../liepin/data/raw_salary.csv',index=None)
    print('转存csv成功')

if __name__ == '__main__':
    run_main_liepin()