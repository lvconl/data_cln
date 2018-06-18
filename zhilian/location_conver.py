#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import numpy as np

def run_main_zhilian():
    city_df = pd.read_table('../zhilian/cln_data/city.csv')
    count_df = pd.read_table('../zhilian/data/count.txt')
    city_list = city_df.values.tolist()
    city_list_df = []
    for item in city_list:
        tmp = item[0].split(',')
        city_list_df.append(tmp)
    count_list = count_df.values.tolist()
    for city,count in zip(city_list_df,count_list):
        print('{\"lng\":' + str(city[1]) + ',\"lat\":' + str(city[2]) + ',\"count\":' + str(count[0]) + '},')

if __name__ == '__main__':
    run_main_zhilian()