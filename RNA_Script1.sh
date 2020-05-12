hisat2-build $1 genome_hisat2_rna

hisat2 -x genome_hisat2_rna -1 $2 -2 $3 -S $4
