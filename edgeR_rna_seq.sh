#!/bin/bash

mkdir $7

Rscript edgeR_testing_2/edgeR_rna_seq.r $1 $2 $3 $4 $5 $6
wait

mv Rplots.pdf $7
mv reads $7
mv toptags_edgeR.csv $7


