# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd

'''
将原始数据转换为标准化的数据

原始数据  1000-1500	1
标准化数据   1250.0,1
'''

def cln_salary(rang_uncln):
    try:
        l_rang = rang_uncln.split('/')
        print(l_rang)
        s_rang = l_rang[0][:len(l_rang[0]) - 1]
        unit = l_rang[0][len(l_rang[0]) - 1:]
        time = l_rang[1]
        avg = 0
        if time == '月':
            if unit == '万':
                rang_str = s_rang.split('-')
                minval = rang_str[0]
                maxval = rang_str[1]
                avg = (float(minval) + float(maxval)) / 2 * 10000
            if unit == '千':
                rang_str = s_rang.split('-')
                minval = rang_str[0]
                maxval = rang_str[1]
                avg = (float(minval) + float(maxval)) / 2 * 1000
        if time == '年':
            if unit == '万':
                rang_str = s_rang.split('-')
                minval = rang_str[0]
                maxval = rang_str[1]
                avg = (float(minval) + float(maxval)) / 2 * 10000 / 12
            if unit == '千':
                rang_str = s_rang.split('-')
                minval = int(rang_str[0])
                maxval = int(rang_str[1])
                avg = (float(minval) + float(maxval)) / 2 * 1000 / 12

        if time == '天':
            avg = float(l_rang[0][:len(l_rang[0]) - 1]) * 30
        if time == '小时':
            avg = float(l_rang[0][:len(l_rang[0]) - 1]) * 30 * 8
            print(avg)
        return avg
    except:
        return 0


def save_to_csv():
    f = open('../qcwy/data/salary.txt','r')
    line = f.readline()
    data = []
    while line:
        tmp = line.strip().split('\t')
        if not tmp[0] == 'NULL' and len(tmp) > 1:
            data.append(tmp)
        line = f.readline()
    data_df = pd.DataFrame(data)
    data_df.columns = ['rang','count']
    data_df.to_csv('../qcwy/data/raw_salary.csv',index=None)
    print('转存csv成功')


def cln_main():
    save_to_csv()
    data = pd.read_csv('../qcwy/data/raw_salary.csv')
    data = data.dropna()


    print(data['rang'].apply(cln_salary))
    data['rang'] = data['rang'].apply(cln_salary)
    df = pd.DataFrame(data)
    data = df.loc[:,'rang':'count']
    df.to_csv('../qcwy/data/cln_data/cln_salary.csv',index=None)
    print(df)


if __name__ == '__main__':
    cln_main()