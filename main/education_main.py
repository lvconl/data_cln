#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import os

from liepin.education_cln import run_main_liepin
from qcwy.educaiton_cln import run_main_qcwy
from zhilian.education_cln import run_main_zhilian

zhilian_path = '../zhilian/education_data/'
qcwy_path = '../qcwy/education_data/'
liepin_path = '../liepin/education_data/'

file_name = 'raw_edu.csv'

def load_data():
    '''
    从不同网站的文件夹加载已经过滤的csv文件
    :return:toget_df
    '''
    zhilian_df = pd.read_csv(os.path.join(zhilian_path,file_name))
    qcwy_df = pd.read_csv(os.path.join(qcwy_path,file_name))
    liepin_df = pd.read_csv(os.path.join(liepin_path,file_name))
    toget_df = pd.concat([zhilian_df,qcwy_df,liepin_df],axis=0,ignore_index=True)
    return toget_df

def edu_static():
    '''
    将数据分类打印
    :return: None
    '''
    edu_df = load_data()
    zhongzhuan_df = edu_df[(edu_df['edu'] == '中专') | (edu_df['edu'] == '中技') | (edu_df['edu'] == '中专/中技及以上')]
    print('中专/中技:{}'.format(sum(zhongzhuan_df['count'].values.tolist())))
    chu_gao_zhong = edu_df[(edu_df['edu'] == '初中') | (edu_df['edu'] == '高中') | (edu_df['edu'] == '初中及以下')]
    print('初/高中:{}'.format(sum(chu_gao_zhong['count'].values.tolist())))
    dazhuan_df = edu_df[(edu_df['edu'] == '大专') | (edu_df['edu'] == '大专及以上')]
    print('大专:{}'.format(sum(dazhuan_df['count'].values.tolist())))
    undergraduate_df = edu_df[(edu_df['edu'] == '本科') | (edu_df['edu'] == '本科及以上') | (edu_df['edu'] == '统招本科')]
    print('本科:{}'.format(sum(undergraduate_df['count'].values.tolist())))
    master_df = edu_df[(edu_df['edu'] == '硕士') | (edu_df['edu'] == '硕士及以上')]
    print('硕士:{}'.format(sum(master_df['count'].values.tolist())))
    phd_df = edu_df[(edu_df['edu'] == '博士')]
    print('博士:{}'.format(sum(phd_df['count'].values.tolist())))
    other_df = edu_df[(edu_df['edu'] == '不限') | (edu_df['edu'] == '学历不限') | (edu_df['edu'] == '其他')]
    print('其他:{}'.format(sum(other_df['count'].values.tolist())))

if __name__ == '__main__':
    run_main_qcwy()
    run_main_zhilian()
    run_main_liepin()
    edu_static()