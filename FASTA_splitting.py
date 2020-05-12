# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:46:33 2019

@author: badhe
"""

import sys

filename = str(sys.argv[1])
infile = open(filename, "r")

base_out = "FASTA/Up_Regulated/"

lines = infile.readlines()
itr = iter(lines)
count = 0

outfile = None

nextline = next(itr)

while(1):
    if(nextline.startswith('>')):
        try:
            outfile.close()
        except AttributeError:
            pass
        count+=1
        outfile = open(base_out+str(count)+".txt", "w+")
        outfile.write(nextline)
    else:
        outfile.write(nextline)
    
    try:
        nextline = next(itr)
    except StopIteration:
        break

outfile.close()
infile.close()

import sys

filename = str(sys.argv[2])
infile = open(filename, "r")

base_out = "FASTA/Down_Regulated/"

lines = infile.readlines()
itr = iter(lines)
count = 0

outfile = None

nextline = next(itr)

while(1):
    if(nextline.startswith('>')):
        try:
            outfile.close()
        except AttributeError:
            pass
        count+=1
        outfile = open(base_out+str(count)+".txt", "w+")
        outfile.write(nextline)
    else:
        outfile.write(nextline)
    
    try:
        nextline = next(itr)
    except StopIteration:
        break

outfile.close()
infile.close()

import sys

filename = str(sys.argv[3])
infile = open(filename, "r")

base_out = "FASTA/Notdiff_Regulated/"

lines = infile.readlines()
itr = iter(lines)
count = 0

outfile = None

nextline = next(itr)

while(1):
    if(nextline.startswith('>')):
        try:
            outfile.close()
        except AttributeError:
            pass
        count+=1
        outfile = open(base_out+str(count)+".txt", "w+")
        outfile.write(nextline)
    else:
        outfile.write(nextline)
    
    try:
        nextline = next(itr)
    except StopIteration:
        break

outfile.close()
infile.close()