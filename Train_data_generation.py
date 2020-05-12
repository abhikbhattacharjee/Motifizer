#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:51:13 2020

@author: badhe
"""

import pandas as pd
base_path = 'Train_requisites/'
base_path1 = 'Excel/'

df3 = pd.read_excel(base_path + 'Up_regulation.xlsx')
df2 = pd.read_excel(base_path + 'Notdiff_regulation.xlsx')
df1 = pd.read_excel(base_path + 'Down_regulation.xlsx')

df3['labels'] = 'up'
df2['labels'] = 'Not_diff'
df1['labels'] = 'Down'


dataset_train = pd.concat([df1, df2, df3], sort = False)
df4 = dataset_train.pop('labels')
dataset_train['labels'] = df4

dataset_train = dataset_train.drop(dataset_train.columns[0], axis = 1)


dataset_train.to_excel(base_path1 + 'combined_train_dataset.xlsx')
