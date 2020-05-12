#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:09:57 2019n

@author: abhik
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#heatmap
df = pd.read_excel("Excel/Final_result.xlsx")
df1 = df[['Unnamed: 0.1','up/down','down/up']]

df2 = df1.loc[df1['up/down'] > 1.5]
df2 = df2.sort_values("up/down",ascending=False)
df2 = df2.head()

df3 = df1.loc[df1['down/up'] > 1.5]
df3 = df3.sort_values("down/up",ascending=False)
df3 = df3.head()

df4 = df1.loc[(df1['Unnamed: 0.1'] == 'Mad') | (df1['Unnamed: 0.1'] == 'Trl') | (df1['Unnamed: 0.1'] == 'mes2') | (df1['Unnamed: 0.1'] == 'hth') ] 

df5 = df1.loc[(df1['down/up'] < 1.5) & (df1['up/down'] < 1.5)].head()

df6 = pd.concat([df2,df3,df4,df5])

heatmap1_data = pd.pivot_table(df6,values = 'down/up', index = ['Unnamed: 0.1'], columns = 'up/down')
plt.figure(figsize = (16,16))
sns.heatmap(heatmap1_data, cmap="coolwarm_r")


def dist_from(ubx_type,pro):
    test = pd.DataFrame()
    test_group_final = pd.DataFrame()
    for dirpath, dirnames, files in os.walk('Output_fimo/Up_regulated_fimo'): #Output_fimo folder
        for file_name in files:
            if file_name.endswith('ubx.xlsx'):
                test = pd.read_excel(dirpath+"/"+str(file_name))
                test = test[test.motif_alt_id== pro]
            
            test_group_final = test_group_final.append(test)
    test_group_final = test_group_final.filter(regex=ubx_type).dropna(how = 'all')
    arr = []
    for i in range(0, len(test_group_final)):
        for j in range(0, len(test_group_final.columns)):
            if(test_group_final.iloc[i][j]>=0 or test_group_final.iloc[i][j]<0):
                arr.append(abs(test_group_final.iloc[i][j]))
    print('arr starts\n')
    print(arr)
    print('arr_ends')
    return arr

def plot_dist(prot):
    ubx = []
    Ubx = []
    ubx = dist_from('ubx',prot)
    Ubx = dist_from('Ubx',prot)
    
# =============================================================================
#     try:
#         sns.distplot(ubx, kde=True)
#         plt.show()
#     except:
#         print(" \n\nHAG DIYA \n\n")
#     
#     try:
#         sns.distplot(Ubx, kde=True)
#         plt.show()
#     except:
#         print(" \n\nHAG DIYA : 1 \n\n")
# =============================================================================
        
    sns.distplot(ubx, kde=True)
    plt.show()
    sns.distplot(ubx, kde=True)
    plt.show()
    plt.hist(ubx, 30)
    plt.show()
    plt.hist(Ubx, 30)
    plt.show()

#plot_dist('pnr')
    
for p in range(1, len(df6)):
    plot_dist(df6['Unnamed: 0.1'][p])



#==============================================================================
# #Gaussian Curve
# mu = 0
# variance = 1
# sigma = math.sqrt(variance)
# 
# x = np.linspace(mu-3 * sigma, mu+3*sigma, 100)
# plt.plot(x, stats.norm.pdf(x, mu, sigma))
# plt.show()
# 
#==============================================================================
