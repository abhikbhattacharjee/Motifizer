import pandas as pd
import sys

peak_calling=pd.read_excel(str(sys.argv[1]), str(sys.argv[4]))
peak_calling['Length'] = peak_calling['End'] - peak_calling['Start'] 

peak_calling1=pd.read_excel(str(sys.argv[1]), str(sys.argv[3]))
peak_calling1['Length'] = peak_calling1['End'] - peak_calling1['Start'] 

peak_calling2=pd.read_excel(str(sys.argv[1]), str(sys.argv[2]))
peak_calling2['Length'] = peak_calling2['End'] - peak_calling2['Start'] 

with pd.ExcelWriter('Excel/Peak_calling_length.xlsx') as writer:
    peak_calling.to_excel(writer, sheet_name='not_diff')
    peak_calling1.to_excel(writer, sheet_name='down_toptags')
    peak_calling2.to_excel(writer, sheet_name='up_toptags')

