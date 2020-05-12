#!/bin/bash
export PATH=$HOME/meme/bin:$PATH

mkdir Output_fimo
mkdir Output_fimo/Prediction_source_fimo
mkdir Excel
mkdir FASTA
mkdir FASTA/Prediction_source
mkdir Train_requisites

python bcd_pred.py $2 $3
mv predict.tsv predict.bed

bedtools slop -i predict.bed -g $4 -b $6 > predict_final.bed        
bedtools getfasta -fi $5 -bed predict_final.bed -fo $7
rm predict.bed

python FASTA_splitting_pred.py $7

for i in FASTA/Prediction_source/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o Output_fimo/Prediction_source_fimo/"fimo$fname" $1 $i
done

for i in Output_fimo/Prediction_source_fimo/*
do	
	python Sort_seq_pred.py $i/*.tsv $i
done

python Peak_calling_length_python_code_pred.py $2 $3
python Tf_analysis_pred.py

wait
python Train_data_generation.py
python final_keras_90acc.py

mkdir $8
mkdir $8/Prediction_results
mkdir $8/Sequences

mv Excel $8/Prediction_results
mv Output_fimo $8/Prediction_results
mv FASTA $8/Prediction_results
mv $7 $8/Sequences
mv predict_final.bed $8/Sequences
