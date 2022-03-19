#!/bin/bash
chmod 777 -R .
mkdir $6

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

bash RNA_Script1.sh $1 $2 $3 hisat2.sam
wait
bash RNA_Script2.sh hisat2.sam hisat2.bam hisat2_filtered.bam
wait
bash RNA_Script3.sh hisat2_filtered.bam $4 $5
wait


mv $5 $6
rm -f hisat2.sam
rm -f hisat2.bam
mv hisat2_filtered.bam $6
#mv genome_hisat2_rna-seq_index $9
mv genome_hisat2_rna* $6
