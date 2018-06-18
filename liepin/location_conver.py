#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

import pandas as pd
import requests
import json

def read_to_csv():
    '''
    读取原始数据并存为csv
    :return: None
    '''
    data = pd.read_table('../liepin/location_data/location_data.txt')
    data.columns = ['location','count']
    data = data.dropna()
    data.to_csv('../liepin/location_data/raw_location.csv',index=None)

def to_coder(location):
    '''
    api_key百度开发者平台申请
    url百度地质转换接口
    将地址转换为经纬度
    :param location: 地址
    :return: lng lat
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    sn = 'I4kVy4mYoghaIKYhgnuzUvFOeBIGpePA'
    #api_key = 'quKzPcQBDVY3awgLpsB6sefjuwT64m0i'
    api_key = 'ww0usZ7UsbDdfhIpQPdRtixP'
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak={}&address={}&sn={}'.format(api_key,location,sn)
    data = requests.get(url,headers = headers)
    result = data.json()
    print(result)
    #纬度
    lng = result['result']['location']['lng']
    #经度
    lat = result['result']['location']['lat']
    return_result = [lng,lat]
    return return_result


def geo_coder_conver():

    data = pd.read_csv('../liepin/location_data/raw_location.csv')
    address_list = data['location'].values.tolist()
    count_list = data['count'].values.tolist()
    print('共{}条数据'.format(len(address_list)))
    city_value = []
    city_lng_lat = []
    i = 1
    for address,count in zip(address_list,count_list):
        print('正在转换第{}条'.format(i))
        try:
            tmp = []
            lng_lat_tmp = to_coder(address)
            lng_lat_tmp.append(address)
            city_lng_lat.append(lng_lat_tmp)
            tmp.append(address)
            tmp.append(count)
            city_value.append(tmp)
            i += 1
        except:
            print('数据{}转换失败'.format(address))
            continue
    for item in city_value:
        print('{name:\'' + str(item[0]) + '\',value:' + str(item[1]) + '},')
    print('-'*40)
    for lng_lat,count in zip(city_lng_lat,city_value):
        print('{\"lng\":' + str(lng_lat[0]) +',\"lat\":'+ str(lng_lat[1]) + ',\"count\":' + str(count[1]) + '},')


def run_main_liepin():
    read_to_csv()
    geo_coder_conver()

if __name__ == '__main__':
    read_to_csv()
    geo_coder_conver()