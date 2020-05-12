#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:58:17 2019

@author: chinmay
"""
import pandas as pd

df = pd.read_excel (r'Excel/Up_regulation.xlsx')

"""df.drop(df.tail(1).index,inplace=True)"""
print (df)

up_sums = df.select_dtypes(pd.np.number).sum().rename('total').to_frame()
df = pd.read_excel (r'Excel/Down_regulation.xlsx')
"""df.drop(df.tail(1).index,inplace=True)"""
print (df)
down_sums = df.select_dtypes(pd.np.number).sum().rename('total').to_frame()

df = pd.read_excel (r'Excel/Notdiff_regulation.xlsx')
"""df.drop(df.tail(1).index,inplace=True)"""
print (df)

diff_sums = df.select_dtypes(pd.np.number).sum().rename('total').to_frame()

overall = pd.concat([diff_sums,up_sums,down_sums],axis=1)
overall.columns = ['not_diff','up','down']
overall.to_excel('Excel/Overall_count_analysis.xlsx')
