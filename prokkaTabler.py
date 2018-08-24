#!/usr/bin/python

import glob

files = glob.glob('*.tsv')
outfile = open("quast.summary","w")
outfile.write("sample\t#contigs>=16bp\ttotalLength>=16bp\t#contigs\tlargestContg\ttotalLength\t%GC\tN50\tN75\tL50\tL75\t#NsPer100kbp\n")

for element in files:
	tsv = open(element,"r").read().split("\n")
	sample = tsv[0].split("\t")[2]
        numContigsG16 = tsv[1].split("\t")[2]
        totalLenG16 = tsv[2].split("\t")[2]
        numContigs = tsv[3].split("\t")[2]
        largestCont = tsv[4].split("\t")[2]
        totalLen = tsv[5].split("\t")[2]
        GC = tsv[6].split("\t")[2]
        N50 = tsv[7].split("\t")[2]
        N75 = tsv[8].split("\t")[2]
        L50 = tsv[9].split("\t")[2]
        L75 = tsv[10].split("\t")[2]
        Np100 = tsv[11].split("\t")[2]
	outfile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\n".format(sample,numContigsG16,totalLenG16,numContigs,largestCont,totalLen,GC,N50,N75,L50,L75,Np100))
outfile.close()		
