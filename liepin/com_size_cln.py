#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import re

f = open('./com_size_data/com_size.txt')
def rece_size():
    '''
    获得与前程无忧相同格式的数据，便于合并分析
    :return: com_size_list
    '''
    file = re.compile('\n')
    com_size_list = []
    line = f.readline()
    while line:
        tmp = line.split('\t')
        tmp[0] = tmp[0][4:len(tmp[0])]
        tmp[1] = file.sub('',tmp[1])
        com_size_list.append(tmp)
        line = f.readline()

    return com_size_list

def save_to_csv():
    com_size_list = rece_size()
    size_df = pd.DataFrame(com_size_list)
    size_df.columns = ['size','count']
    size_df.to_csv('./com_size_data/raw_cln_com_size.csv', index=None)
    print('转存csv成功！')

if __name__ == '__main__':
    save_to_csv()