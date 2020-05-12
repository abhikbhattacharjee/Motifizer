#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:09:57 2019

@author: abhik
"""

import os
import pandas as pd
#import sys

test_group_final = pd.DataFrame()

for dirpath, dirnames, files in os.walk('Output_fimo/Up_regulated_fimo'): #Output_fimo folder
    for file_name in files:
        if file_name.endswith('_fimo.xlsx'):
            test = pd.read_excel(dirpath+"/"+str(file_name)) 
            
            path = os.path.dirname(dirpath+"/"+str(file_name))
            basename1 = os.path.basename(path)
            columns1 = test['motif_alt_id'].unique()
            
            test_group = test.groupby(['motif_alt_id']).size().reset_index(name=basename1)
            count1 = test_group[basename1]
                        
            test_group.index = test_group.loc[:,'motif_alt_id']
            test_group = test_group.drop(['motif_alt_id'],axis = 1)
            test_group = test_group.T
            
            test_group_final=test_group_final.append(test_group,sort=False)
test_group_final=test_group_final.sort_index(axis=0)
test_group_final=test_group_final.fillna(0)
test_group_final.to_excel("Excel/Up_regulation.xlsx",sheet_name="Up_regulation")

