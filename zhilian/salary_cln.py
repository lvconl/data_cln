#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷
import numpy as np
import pandas as pd

'''
将原始数据转换为标准化的数据

原始数据  1000-1500	1
标准化数据   1250.0,1
'''


f = open('data/salary.txt','r')
def run_main():
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
    print(salary_avg_count_list)


    data = pd.DataFrame(salary_avg_count_list)
    data.columns = ['rang','count']
    data.to_csv('cln_data/cln_salary.csv',index=None)
