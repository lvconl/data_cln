#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__:吕从雷

from liepin.location_conver import run_main_liepin
from qcwy.location_conver import run_main_qcwy
from zhilian.location_conver import run_main_zhilian



if __name__ == '__main__':
    '''
    因执行较慢，且数据执行过程中需要观测是否有异常
    请分别执行三个函数
    '''
    #run_main_zhilian()
    #run_main_qcwy()
    run_main_liepin()