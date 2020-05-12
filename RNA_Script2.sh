samtools view -S -b $1 > $2
wait
samtools view -F 0x200 -F 0x4 -b $2 > $3
