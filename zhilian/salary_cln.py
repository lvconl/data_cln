#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import numpy as np
import pandas as pd
import os

'''
将原始数据转换为标准化的数据

原始数据  1000-1500	1
标准化数据   1250.0,1
'''
file_path = '../zhilian/data/salary_filte.txt'

f = open('../zhilian/data/salary.txt','r')

def rang_flite():
    line = f.readline()
    s = open(file_path,'w')
    while line:
        if (line == '1000元以下') and (line == '25000元以上'):
            print(line)
            continue
        if (not line[0] == '学') and (not line[0] == '数') and (not line[0] == '深') and (not line[0] == '经') and (not line[0] == '面') and (not line[0] == '\t') and (not line.split('\t')[0][len(line.split('\t')[0]) - 1] == '上') and(not line.split('\t')[0][len(line.split('\t')[0]) - 1] == '下'):
            s.write(line)
        line = f.readline()

def run_main_zhilian():
    rang_flite()
    f = open('../zhilian/data/salary_filte.txt','r')
    line = f.readline()
    salary_avg_count_list = []
    salary_avglist = []
    while line:
        list = []
        salary = line.split()
        salary_rang = salary[0].split('-')
        salary_count = int(salary[1])
        salary_min = int(salary_rang[0])
        salary_max = int(salary_rang[1])
        salary_avg = np.array([salary_max,salary_min]).mean()
        list.append(salary_avg)
        salary_avglist.append(salary_avg)
        list.append(salary_count)
        salary_avg_count_list.append(list)
        line = f.readline()

    data = pd.DataFrame(salary_avg_count_list)
    print(data)
    data.columns = ['rang','count']
    print(data)
    data.to_csv('../zhilian/cln_data/cln_salary.csv',index=None)

if __name__ == '__main__':
    run_main_zhilian()
