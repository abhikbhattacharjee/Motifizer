#!/bin/bash
chmod 777 -R .
mkdir $5



hisat2-build $1 genome_hisat2_rna
hisat2 -x genome_hisat2_rna -U $2 -S hisat2_SE.sam
wait

samtools view -S -b hisat2_SE.sam > hisat2_SE.bam
wait
samtools view -F 0x200 -F 0x4 -b hisat2_SE.bam > hisat2_filtered_SE.bam
wait

htseq-count --format=bam --stranded=no --type=exon hisat2_filtered_SE.bam $3 > $4

wait


mv $4 $5
rm -f hisat2_SE.sam
rm -f hisat2_SE.bam
mv hisat2_filtered_SE.bam $5
#mv genome_hisat2_rna-seq_index $9
mv genome_hisat2_rna* $5
