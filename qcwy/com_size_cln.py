#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

'''
用来将前程无忧从hive里导出的数据清晰，转换为可视化可用的数据
'''
import pandas as pd
import re

f = open('./com_size_data/com_size.txt')


def load_data_to_list():
    '''
    加载原始数据，
    :return:
    '''
    file = re.compile('\n')
    line = f.readline()
    com_size_list = []
    while line:
        try:
            if int(line[0]):
                line = file.sub('',line)
                com_size_list.append(line)
        except:
            pass
        line = f.readline()
    return com_size_list

def split_size_count():
    com_size_list = load_data_to_list()
    result_list = []
    for item in com_size_list:
        tmp = item.split('\t')
        result_list.append(tmp)
    return result_list

def save_to_csv():
    com_size_list = split_size_count()
    size_df = pd.DataFrame(com_size_list)
    size_df.columns = ['size','count']
    size_df.to_csv('./com_size_data/raw_com_size.csv',index=None)
    print('转存csv成功')


def run_main():
    save_to_csv()
    com_size_list = split_size_count()
    for item in com_size_list:
        print('{}\t{}'.format(item[0],item[1]))

if __name__ == '__main__':
    run_main()
