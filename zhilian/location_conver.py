#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import numpy as np

city_df = pd.read_table('./cln_data/city.csv')
count_df = pd.read_table('./data/count.txt')
print(count_df)

city_list = city_df.values.tolist()

city_list_df = []

for item in city_list:
    tmp = item[0].split(',')
    city_list_df.append(tmp)

count_list = count_df.values.tolist()

print(city_list_df)

for city,count in zip(city_list_df,count_list):
    print('{\"lng\":' + str(city[1]) + ',\"lat\":' + str(city[2]) + ',\"count\":' + str(count[0]) + '},')