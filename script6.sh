#!/bin/bash
bwa mem $1 $3 > bwa_input
samtools view -S -b bwa_input > bwa_input.bam
samtools view -F 0x200 -F 0x4 -b bwa_input.bam > bwa_input_filtered.bam

