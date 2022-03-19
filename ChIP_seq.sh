#!/bin/bash
sudo chmod 777 -R .
bwa index $1
wait

parallel --link bash ::: script5.sh script6.sh ::: $1 $1 ::: $2 $3 
#bash script5.sh $1 $2
#bash script6.sh $1 $3
wait

macs2 callpeak -t bwa_test_filtered.bam -c bwa_input_filtered.bam --outdir macs2 --format AUTO --gsize dm --pvalue 0.05 --call-summits
annotatePeaks.pl macs2/NA_summits.bed none -gtf $4 -noblanks > homer_data
#annotatePeaks.pl macs2/NA_summits.bed -gtf $4 -noblanks > homer_data.xlsx

findMotifsGenome.pl macs2/NA_summits.bed $1 output_motif -mask -size 200m -mset insect

mkdir $5
mv homer_data $5
#mv homer_data.xlsx $5
mv macs2 $5 
mv bwa_test_filtered.bam $5
mv bwa_input_filtered.bam $5
mv output_motif $5

mv $1 $5
mv $2 $5
mv $3 $5
mv $4 $5


