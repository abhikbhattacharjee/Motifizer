# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import pandas as pd
import os

test = pd.read_csv(str(sys.argv[1]),delimiter='\t',encoding='utf-8') 

sorted_values = test.sort_values("motif_alt_id", ascending = True)

print(sorted_values)
out_path = str(sys.argv[2])
print(out_path)

filename = "sorted_values_fimo.xlsx"
sorted_values.to_excel(os.path.join(out_path,filename), index=False)


df=pd.read_excel(os.path.join(out_path,filename))
print(df[df.motif_alt_id=="denovo_ubx"])

df['mean'] = (df['start']+df['stop'])/2
print(df['mean'])

for i in df[df.motif_alt_id=="denovo_ubx"].index:
    df["diff_denovo_ubx"+str(i)] = df['mean'] - df.iloc[i]['mean']
    
    
for i in df[df.motif_alt_id=="Ubx"].index:
    df["diff_Ubx"+str(i)] = df['mean'] - df.iloc[i]['mean']
    
    
filename1 = "Dist_from_ubx.xlsx"
df = df.to_excel(os.path.join(out_path,filename1))
