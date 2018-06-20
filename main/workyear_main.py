#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import os

from zhilian.workyear_cln import run_main_zhilian
from liepin.workyear_cln import run_main_liepin
from qcwy.workyear_cln import run_main_qcwy

zhilian_path = '../zhilian/workyear_data/'
qcwy_path = '../qcwy/workyear_data/'
liepin_path = '../liepin/workyear_data/'

file_name = 'raw_work.csv'

def load_data_from_csv():
    '''
    分别从不同网站中加载csv文件
    :return: toget_df
    '''
    zhilian_df = pd.read_csv(os.path.join(zhilian_path,file_name))
    qcwy_df = pd.read_csv(os.path.join(qcwy_path,file_name))
    liepin_df = pd.read_csv(os.path.join(liepin_path,file_name))
    toget_df = pd.concat([zhilian_df,qcwy_df,liepin_df],ignore_index=True)
    return toget_df

def year_static():
    toget_df = load_data_from_csv()
    zero_df = toget_df[(toget_df['work'] == '无经验') | (toget_df['work'] == '无工作经验') | (toget_df['work'] == '1年以下')]
    print('无经验:{}'.format(sum(zero_df['count'].values.tolist())))
    one_to_three_df = toget_df[(toget_df['work'] == '1-3年') | (toget_df['work'] == '1年经验') | (toget_df['work'] == '2年经验') | (toget_df['work'] == '1年以上') | (toget_df['work'] == '2年以上')]
    print('1-3年:{}'.format(sum(one_to_three_df['count'].values.tolist())))
    three_to_five_df = toget_df[(toget_df['work'] == '3-5年') | (toget_df['work'] == '3-4年经验') | (toget_df['work'] == '3年以上') | (toget_df['work'] == '4年以上')]
    print('3-5年:{}'.format(sum(three_to_five_df['count'].values.tolist())))
    five_to_ten_df = toget_df[(toget_df['work'] == '5-10年') | (toget_df['work'] == '8-9年经验') | (toget_df['work'] == '5-7年经验') | (toget_df['work'] == '5年以上') | (toget_df['work'] == '6年以上') | (toget_df['work'] == '7年以上') | (toget_df['work'] == '8年以上')]
    print('5-10:{}'.format(sum(five_to_ten_df['count'].values.tolist())))
    more_ten_df = toget_df[(toget_df['work'] == '10年以上') | (toget_df['work'] == '10年以上经验') | (toget_df['work'] == '12年以上') | (toget_df['work'] == '15年以上') | (toget_df['work'] == '33年以上')]
    print('10年以上:{}'.format(sum(more_ten_df['count'].values.tolist())))
    other_df = toget_df[toget_df['work'] == '经验不限']
    print('经验不限:{}'.format(sum(other_df['count'].values.tolist())))

def run_main():
    run_main_zhilian()
    run_main_qcwy()
    run_main_liepin()

if __name__ == '__main__':
    run_main()
    year_static()