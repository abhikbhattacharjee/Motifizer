#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:43:52 2019

@author: abhik
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_excel("Excel/Final_result.xlsx")
df1 = df[['Unnamed: 0.1','up/down','down/up']]

df2 = df1.loc[df1['up/down'] > 1.5]
df2 = df2.sort_values("up/down",ascending=False)
df2 = df2.head()

df3 = df1.loc[df1['down/up'] > 1.5]
df3 = df3.sort_values("down/up",ascending=False)
df3 = df3.head()

df4 = df1.loc[(df1['Unnamed: 0.1'] == 'Mad') | (df1['Unnamed: 0.1'] == 'Trl') | (df1['Unnamed: 0.1'] == 'mes2') | (df1['Unnamed: 0.1'] == 'hth')] 

df5 = df1.loc[(df1['down/up'] < 1.5) & (df1['up/down'] < 1.5)].head()

df6 = pd.concat([df2,df3,df4,df5])

heatmap1_data = pd.pivot_table(df6, values = 'down/up', index = ['Unnamed: 0.1'], columns = 'up/down')
plt.figure(figsize = (16,16))
sns.heatmap(heatmap1_data, cmap="coolwarm_r")

