#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse
prog = re.compile(r"(\d+)([MISDHN])")




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

def write(n,s,sl):
	print(">"+n)
	c=0
	while(c<len(s)):
		print(s[c:c+sl])
		c+=sl



parser.add_argument("--width", type=int, required=False, dest="width", default="80", help="width of sequence")
args = parser.parse_args()






for line in sys.stdin:
	objid,header,seq = line.rstrip("\n").split("\t")
	if(objid!="fasta"):
		raise Excpetion("Invalid input stream, must be fasta-object")
	
	write(header,seq,args.width)
