#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse
prog = re.compile(r"(\d+)([MISDHN])")




parser = argparse.ArgumentParser(description="""           
Fastq filter:
functions:
- filter minimum length
- filter maximum length
.. many more possible
""",formatter_class=argparse.RawDescriptionHelpFormatter,
epilog="""
Authors
-------
    Robert Kofler
""")
parser.add_argument("--min-len", type=int, required=False, dest="minlen", default=None, help="minimum length of read")
parser.add_argument("--max-len", type=int, required=False, dest="maxlen", default=None, help="maximum length of read")
args = parser.parse_args()



for line in sys.stdin:
	line=line.rstrip("\n")
	objid,h1,seq,h2,qual = line.split("\t")
	if(objid!="fastq"):
		raise Excpetion("Invalid input stream, must be fastq-object")
	if(args.minlen is not None and len(seq)< args.minlen):
		continue
	if(args.maxlen is not None and len(seq)>args.maxlen):
		continue
	print line

