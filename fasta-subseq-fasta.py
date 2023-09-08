#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse
import collections




parser = argparse.ArgumentParser(description="""           
Fasta writter:
functions:
converts to fasta file format
""",formatter_class=argparse.RawDescriptionHelpFormatter,
epilog="""
Authors
-------
    Robert Kofler
""")

def load_bed(f):
	sh=collections.defaultdict(lambda:[])
	for l in open(f):
		l=l.rstrip("\n")
		chrm,start,end,name=re.split(r"[ \t]",l)
		sh[chrm].append([int(start),int(end),name])
	return sh

parser.add_argument("--bed", type=str, required=False, dest="bed", default="" ,help="subsequences to load")
parser.add_argument("--fasta-ids", type=str, required=False, dest="faid", default="", help="a comma separated list of fasta-IDs that will be kept")
args = parser.parse_args()

if(args.bed!=""):
	subh=load_bed(args.bed)
	for line in sys.stdin:
		objid,header,seq = line.rstrip("\n").split("\t")
		if header in subh:
			for start,end,name in subh[header]:
				newseq=seq[start-1:end]
				topr=["fasta",name,newseq]
				print("\t".join(topr))
elif(args.faid!=""):
	tocheck=set([])
	if("," in args.faid):
		tocheck=set(args.faid.split(","))
	else:
		tocheck=set([args.faid])
	for line in sys.stdin:
		objid,header,seq = line.rstrip("\n").split("\t")
		if header in tocheck:
			topr=["fasta",header,seq]
			print("\t".join(topr))
		
	
else:
	raise Exception("invalid mode, either bed or fastaid must be provided")
	
