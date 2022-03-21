#!/bin/bash
chmod 777 -R .
mkdir $6

echo "Motifizer: Making index file"
hisat2-build $1 genome_hisat2_rna

echo "Motifizer: Constructing SAM File"
hisat2 -x genome_hisat2_rna -1 $2 -2 $3 -S hisat2.sam
wait

echo "Motifizer: Converting SAM file to BAM file"
samtools view -S -b hisat2.sam > hisat2.bam
wait

echo "Motifizer: BAM Filtering in Process"
samtools view -F 0x200 -F 0x4 -b hisat2.bam > hisat2_filtered.bam
wait

echo "Motifizer: Performing read counts"
htseq-count --format=bam --stranded=no --type=exon hisat2_filtered.bam $4 > $5
wait

echo "Motifizer: File management -> Output Directory Path"
mv $5 $6
rm -f hisat2.sam
rm -f hisat2.bam
mv hisat2_filtered.bam $6
mv genome_hisat2_rna* $6

echo "Process Complete. Please check the output folder"
