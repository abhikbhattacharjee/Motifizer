#!/bin/bash
python Peak_calling_length_python_code.py $1 $2 $3 $4
python Tf_analysis.py
python Tf_analysis1.py
python TF_analysis2.py
python Overall_count_analysis.py	
python Frequency_analysis.py
#python3 dist_measure.py
