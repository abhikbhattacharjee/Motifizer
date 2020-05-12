#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

library(edgeR)

files <- c(args[1],args[2],args[3],args[4],args[5],args[6])
class <- c("test", "test", "test", "cont", "cont", "cont")
label <- c("HD1", "HD2", "HD3", "WD1", "WD2", "WD3")

counts <- readDGE(files=files, group=class, labels=label)

noint = rownames(counts) %in% c("no_feature", "ambiguous", "too_low_aQual", "not_aligned", "alignment_not_unique")
cpms =cpm(counts)
keep = rowSums(cpms>1) >=2 & !noint ###############################################################note here: count needs to be one in atleast 2 samples
counts = counts [keep,]

d = DGEList (counts=counts, group=class)
d= calcNormFactors (d)

plotMDS (d, labels=label, col=c("darkgreen", "blue") [factor(class)])

d= estimateCommonDisp(d)
d=estimateTagwiseDisp(d)

plotMeanVar(d, show.tagwise.vars=TRUE, NBline=TRUE)
plotBCV(d)

de = exactTest(d, pair=c("test", "cont"))
tt= topTags (de, n=nrow(d))
nc  =  cpm(d, normalized.lib.sizes = TRUE)
rn  =  rownames(tt$table)

head(nc[rn,order(class)],5)

deg  =  rn[tt$table$FDR  <  .05]
plotSmear(d, de.tags = deg)

write.csv(tt$table, file =  "toptags_edgeR.csv" )
write.csv(nc, file =  "reads" )
