#!/bin/bash
bwa index $1
wait

parallel --link bash ::: script5.sh script6.sh ::: $1 $1 ::: $2 $3 
#bash script5.sh $1 $2
#bash script6.sh $1 $3
wait

macs2 callpeak -t bwa_test_filtered.bam -c bwa_test_input_filtered.bam --outdir macs2
annotatePeaks.pl macs2/NA_summits.bed $4 -noblanks > homer_data
annotatePeaks.pl macs2/NA_summits.bed $4 -noblanks > homer_data.xlsx

mkdir $5
mv homer_data $5
mv homer_data.xlsx $5





