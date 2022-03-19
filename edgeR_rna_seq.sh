#!/bin/bash
chmod 777 -R .
mkdir $7

Rscript edgeR_testing_2/edgeR_rna_seq.r $1 $2 $3 $4 $5 $6
wait

mv Rplots.pdf $7
mv reads $7
mv toptags_edgeR.csv $7

mv $1 $7
mv $2 $7
mv $3 $7
mv $4 $7
mv $5 $7
mv $6 $7


