# -*- coding: utf-8 -*-
# @File  : preprocess.py
# @Author: oaapao
# @Date  : 2022/12/9 15:18
# @Desc  :
# @Contact : zhiqiang.shen@zju.edu.cn

import pandas as pd

train_data = pd.read_csv('data/train.csv', sep=' ')
test_data = pd.read_csv('data/test.csv', sep=' ')

# 输出数据的大小信息
print('Train data shape:', train_data.shape)
print('TestA data shape:', test_data.shape)

train_data.head()
