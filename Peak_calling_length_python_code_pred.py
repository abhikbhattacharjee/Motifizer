import pandas as pd

peak_calling=pd.read_excel("Peakcalling_1e-4__PePr_peaks_homer.xlsx",'Peakcalling_1e-4__PePr_peaks_ho')
peak_calling['Length'] = peak_calling['End'] - peak_calling['Start'] 

with pd.ExcelWriter('Excel/Peak_calling_length.xlsx') as writer:
    peak_calling.to_excel(writer, sheet_name='Prediction')

