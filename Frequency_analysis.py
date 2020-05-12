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

frequency_data=pd.read_excel("Excel/Overall_count_analysis.xlsx")

frequency_data['notdiff_frequency']=(frequency_data['not_diff']*1000)/((round(mean_notdiff)+400)*count1)
frequency_data['down_frequency']=(frequency_data['down']*1000)/((round(mean_downtags)+  400)*count2)
frequency_data['up_frequency']=(frequency_data['up']*1000)/((round(mean_uptags)+400)*count3)

frequency_data = frequency_data.to_excel("Excel/frequency_analysis.xlsx")
frequency_data1=pd.read_excel("Excel/frequency_analysis.xlsx")

frequency_data1['up/down'] = frequency_data1['up_frequency']/frequency_data1['down_frequency']
frequency_data1['down/up'] = frequency_data1['down_frequency']/frequency_data1['up_frequency']

frequency_data1['up/not_diff'] = frequency_data1['up_frequency']/frequency_data1['notdiff_frequency']
frequency_data1['not_diff/up'] = frequency_data1['notdiff_frequency']/frequency_data1['up_frequency']

frequency_data1['down/not_diff'] = frequency_data1['down_frequency']/frequency_data1['notdiff_frequency']
frequency_data1['not_diff/down'] = frequency_data1['notdiff_frequency']/frequency_data1['down_frequency']

frequency_data1 = frequency_data1.to_excel("Excel/Final_result.xlsx")
