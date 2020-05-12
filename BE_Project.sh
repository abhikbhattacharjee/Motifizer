#!/bin/bash
a=1
export PATH=$HOME/meme/bin:$PATH

mkdir FASTA
mkdir FASTA/Up_Regulated
mkdir FASTA/Down_Regulated
mkdir FASTA/Notdiff_Regulated
mkdir Output_fimo
mkdir Output_fimo/Up_regulated_fimo
mkdir Output_fimo/Down_regulated_fimo
mkdir Output_fimo/Notdiff_regulated_fimo
mkdir Excel
#mkdir Subplots

python bcd.py $2 $3 $4 $5

mv not.tsv not.bed
mv up.tsv up.bed
mv down.tsv down.bed

bedtools slop -i up.bed -g $6 -b $8 > up_final.bed        
bedtools getfasta -fi $7 -bed up_final.bed -fo $9
rm up.bed

bedtools slop -i down.bed -g $6 -b $8 > down_final.bed        
bedtools getfasta -fi $7 -bed down_final.bed -fo ${10}
rm down.bed

bedtools slop -i not.bed -g $6 -b $8 > not_final.bed        
bedtools getfasta -fi $7 -bed not_final.bed -fo ${11}
rm not.bed

python FASTA_splitting.py $9 ${10} ${11} 

parallel --link bash {1} {2} {3} ::: script1.sh script2.sh script3.sh ::: $1 $1 $1 
wait
bash script4.sh $2 $3 $4 $5

mkdir ${12}
mkdir ${12}/Sequence_files

mv FASTA ${12}
mv Output_fimo ${12}
mv not_final.bed ${12}/Sequence_files
mv up_final.bed ${12}/Sequence_files
mv down_final.bed ${12}/Sequence_files
mv $9 ${12}/Sequence_files
mv ${10} ${12}/Sequence_files
mv ${11} ${12}/Sequence_files
mv Excel ${12}

