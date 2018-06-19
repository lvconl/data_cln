#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import os

from zhilian.salary_cln import run_main_zhilian
from liepin.salary_cln import run_main_liepin
from qcwy.salary_cln import cln_main

'''
来自不同网站的数据的路径
'''
zhilian_path = '../zhilian/cln_data/'
qcwy_path = '../qcwy/data/cln_data'
liepin_path = '../liepin/data/cln_data'

'''
文件名
'''
salary_file_name = 'cln_salary.csv'

def load_data():
    '''
    合并来自不同网站的已经清洗的csv文件
    :return: toget_df
    '''
    salary_from_zhilian = pd.read_csv(os.path.join(zhilian_path,salary_file_name))
    salary_from_qcwy = pd.read_csv(os.path.join(qcwy_path,salary_file_name))
    salary_from_liepin = pd.read_csv(os.path.join(liepin_path,salary_file_name))

    salary_from_qcwy_df = pd.DataFrame(salary_from_qcwy)
    salary_from_zhilian_df = pd.DataFrame(salary_from_zhilian)
    salary_from_liepin_df = pd.DataFrame(salary_from_liepin)

    toget_df = pd.concat([salary_from_zhilian_df,salary_from_qcwy_df,salary_from_liepin_df],axis=0,ignore_index=True)
    #toget_df = toget_df.reset_index()
    print(toget_df)
    return toget_df


def rang_count():
    '''
    统计不同工资段的数目
    :return: None
    '''
    data_df = load_data()
    zero_count_df = data_df[data_df['rang'] < 1000]
    print('1000以下: ' + str(zero_count_df.apply(sum)['count']))
    one_count_df = data_df[(data_df['rang'] >= 1000) & (data_df['rang'] <= 3000)]
    print('1000-3000: ' + str(one_count_df.apply(sum)['count']))
    two_count_df = data_df[(data_df['rang'] > 3000) & (data_df['rang'] <= 5000)]
    print('3000-5000: ' + str(two_count_df.apply(sum)['count']))
    three_count_df = data_df[(data_df['rang'] > 5000) & (data_df['rang'] <= 7000)]
    print('5000-7000: ' + str(three_count_df.apply(sum)['count']))
    four_count_df = data_df[(data_df['rang'] > 7000) & (data_df['rang'] <= 9000)]
    print('7000-9000: ' + str(four_count_df.apply(sum)['count']))
    five_count_df = data_df[(data_df['rang'] > 9000) & (data_df['rang'] <= 11000)]
    print('9000-11000: ' + str(five_count_df.apply(sum)['count']))
    six_count_df = data_df[(data_df['rang'] > 11000) & (data_df['rang'] <= 13000)]
    print('11000-13000: ' + str(six_count_df.apply(sum)['count']))
    seven_count_df = data_df[(data_df['rang'] > 13000) & (data_df['rang'] <= 15000)]
    print('13000-15000: ' + str(seven_count_df.apply(sum)['count']))
    eight_count_df = data_df[(data_df['rang'] > 15000) & (data_df['rang'] <= 17000)]
    print('15000-17000: ' + str(eight_count_df.apply(sum)['count']))
    nine_count_df = data_df[(data_df['rang'] > 17000) & (data_df['rang'] <= 19000)]
    print('17000-19000: ' + str(nine_count_df.apply(sum)['count']))
    ten_count_df = data_df[(data_df['rang'] > 19000) & (data_df['rang'] <= 21000)]
    print('19000-21000: ' + str(ten_count_df.apply(sum)['count']))
    eleven_count_df = data_df[(data_df['rang'] > 21000) & (data_df['rang'] <= 23000)]
    print('21000-23000: ' + str(eleven_count_df.apply(sum)['count']))
    twelen_count_df = data_df[(data_df['rang'] > 23000) & (data_df['rang'] <= 25000)]
    print('23000-25000: ' + str(twelen_count_df.apply(sum)['count']))
    thirteen_count_df = data_df[data_df['rang'] > 25000]
    print('25000以上:' + str(thirteen_count_df.apply(sum)['count']))
    salary_list = data_df['rang'].values.tolist()
    count_list = data_df['count'].values.tolist()
    acc = 0
    for salary,count in zip(salary_list,count_list):
        acc += salary * count
    print('平均工资:{}'.format(acc / sum(count_list)))


def run_main():
    run_main_zhilian()
    run_main_liepin()
    cln_main()
    rang_count()

if __name__ == '__main__':
    run_main()