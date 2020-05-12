#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:16:09 2019

@author: chinmay
"""

import pandas as pd
import sys

p_c=pd.read_excel(str(sys.argv[1]), str(sys.argv[4]))
p_c_down=pd.read_excel(str(sys.argv[1]), str(sys.argv[3]))
p_c_up=pd.read_excel(str(sys.argv[1]), str(sys.argv[2]))

cols = [1,2,3]

df = p_c[p_c.columns[cols]]
#df=df.sample(n=258)
df.to_csv(path_or_buf="not.tsv",sep='\t',index=False,header=False)

df = p_c_down[p_c_down.columns[cols]]
#df=df.sample(n=93)
df.to_csv(path_or_buf="down.tsv",sep='\t',index=False,header=False)

df = p_c_up[p_c_up.columns[cols]]
#df=df.sample(n=129)
df.to_csv(path_or_buf="up.tsv",sep='\t',index=False,header=False)
