# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:22:53 2019

@author: Abhik
"""

import pandas as pd

peak_calling=pd.read_excel("Excel/Peak_calling_length.xlsx", 'not_diff')
peak_calling1=pd.read_excel("Excel/Peak_calling_length.xlsx", 'down_toptags')
peak_calling2=pd.read_excel("Excel/Peak_calling_length.xlsx", 'up_toptags')

mean_notdiff = peak_calling['Length'].mean() 
count1 = peak_calling['Length'].count() 
mean_downtags = peak_calling1['Length'].mean()
count2 = peak_calling1['Length'].count()
mean_uptags = peak_calling2['Length'].mean()
count3 = peak_calling2['Length'].count()

#Column Names
eg1 = 'Enhancer_Group1'
eg2 = 'Enhancer_Group2'
eg3 = 'Enhancer_Group3'
eg1f = 'Enhancer_Group1_frequency'
eg2f = 'Enhancer_Group2_frequency'
eg3f = 'Enhancer_Group3_frequency'

frequency_data=pd.read_excel("Excel/Overall_count_analysis.xlsx")
frequency_data.rename(columns = {'not_diff':eg3, 'down':eg2, 'up':eg1,'Unnamed: 0':'Transcription_Factor'}, inplace = True)

frequency_data[eg3f]=(frequency_data[eg3]*1000)/((round(mean_notdiff)+400)*count1)
frequency_data[eg2f]=(frequency_data[eg2]*1000)/((round(mean_downtags)+  400)*count2)
frequency_data[eg1f]=(frequency_data[eg1]*1000)/((round(mean_uptags)+400)*count3)

frequency_data = frequency_data.to_excel("Excel/frequency_analysis.xlsx")
frequency_data1=pd.read_excel("Excel/frequency_analysis.xlsx")

frequency_data1[str(eg1)+'/'+str(eg2)] = frequency_data1[eg1f]/frequency_data1[eg2f]
frequency_data1[str(eg2)+'/'+str(eg1)] = frequency_data1[eg2f]/frequency_data1[eg1f]

frequency_data1[str(eg1)+'/'+str(eg3)] = frequency_data1[eg1f]/frequency_data1[eg3f]
frequency_data1[str(eg3)+'/'+str(eg1)] = frequency_data1[eg3f]/frequency_data1[eg1f]

frequency_data1[str(eg2)+'/'+str(eg3)] = frequency_data1[eg2f]/frequency_data1[eg3f]
frequency_data1[str(eg3)+'/'+str(eg2)] = frequency_data1[eg3f]/frequency_data1[eg2f]

frequency_data1 = frequency_data1.drop(columns='Unnamed: 0')
frequency_data1 = frequency_data1.to_excel("Excel/Final_result.xlsx")