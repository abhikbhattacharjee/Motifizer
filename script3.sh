#!/bin/bash
export PATH=$HOME/meme/bin:$PATH

for i in FASTA/Notdiff_Regulated/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o Output_fimo/Notdiff_regulated_fimo/"fimo$fname" $1 $i
done

for i in Output_fimo/Notdiff_regulated_fimo/*
do	
	python Sort_seq.py $i/*.tsv $i
done
	
