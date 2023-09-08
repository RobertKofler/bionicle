#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse


parser = argparse.ArgumentParser(description="""           
Description
-----------
Summary statistics
""",formatter_class=argparse.RawDescriptionHelpFormatter,
epilog="""
Authors
-------
    Robert Kofler
""")
#parser.add_argument('--fastq', type=str, default=None,dest="fasta", required=True, help="A fasta file")

args,unknown = parser.parse_known_args()
fh=None
if(len(unknown)>0):
	fh=open(unknown[0])
else:
	fh=sys.stdin

while(True):
	h1=fh.readline()
	if h1 =="":
		break
	h1=h1.rstrip("\n").split(" ")[0]
	seq=fh.readline().rstrip("\n")
	h2=fh.readline().rstrip("\n")
	qual=fh.readline().rstrip("\n")
	
	
	topr=["fastq",h1,seq,h2,qual]
	print("\t".join(topr))