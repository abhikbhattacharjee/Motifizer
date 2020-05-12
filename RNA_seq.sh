#!/bin/bash

mkdir $9

#hisat2-build $1 genome_hisat2_rna-seq_index
#wait
#hisat2 -x genome_hisat2_rna-seq -1 $2 -2 $3 -S $4
#wait
#samtools view -S -b $4 > $5
#wait
#samtools view -F 0x200 -F 0x4 -b $5 > $6
#wait
#htseq-count --format=bam --stranded=no --type=exon $6 $7 > $8
#wait

bash RNA_Script1.sh $1 $2 $3 $4
wait
bash RNA_Script2.sh $4 $5 $6
wait
bash RNA_Script3.sh $6 $7 $8
wait


mv $8 $9
mv $4 $9
mv $5 $9
mv $6 $9
#mv genome_hisat2_rna-seq_index $9
mv genome_hisat2_rna* $9
