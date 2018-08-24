#!/usr/bin/python

import glob

files = glob.glob('*.txt')
outfile = open("prokka.summary","w")
outfile.write("sample\tcontigs\tbases\tCDS\trepeat_region\ttRNA\ttmRNA\n")

for element in files:
	sample = element.replace(".txt","")
	tsv = open(element,"r").read().split("\n")
	for line in tsv:
		if "contigs:" in line:
			contigs = line.split(" ")[1]
                elif "bases:" in line:
		        bases = line.split(" ")[1]
                elif "CDS:" in line:
		        CDS = line.split(" ")[1]
                elif "repeat_region:" in line:
		        repeat_region = line.split(" ")[1]
                elif "tRNA:" in line:
		        tRNA = line.split(" ")[1]
                elif "tmRNA:" in line:
		        tmRNA = line.split(" ")[1]
	outfile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format(sample,contigs,bases,CDS,repeat_region,tRNA,tmRNA,))
outfile.close()		
