#!/bin/bash
chmod 777 -R .

macs2 callpeak -t $1 -c $2 --outdir macs2 --format AUTO --gsize dm --pvalue 0.05 --call-summits
annotatePeaks.pl macs2/NA_summits.bed none -gtf $3 -noblanks > homer_data
#annotatePeaks.pl macs2/NA_summits.bed -gtf $3 -noblanks > homer_data.xlsx

findMotifsGenome.pl macs2/NA_summits.bed $5 output_motif -mask -size 200m -mset insect

mkdir $4
mv homer_data $4
#mv homer_data.xlsx $4
mv macs2 $4

mv $1 $4
mv $2 $4
mv $3 $4
mv $5 $4
mv output_motif $4
