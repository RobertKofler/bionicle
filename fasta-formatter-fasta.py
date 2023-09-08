#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse
prog = re.compile(r"(\d+)([MISDHN])")




parser = argparse.ArgumentParser(description="""           
Fasta formatter:
functions:
- convert to upper case
- convert to lower case
- mask region
""",formatter_class=argparse.RawDescriptionHelpFormatter,
epilog="""
Authors
-------
    Robert Kofler
""")
parser.add_argument('--upper',dest="upper", action='store_true',  help="convert everything to upper case")
args = parser.parse_args()



for line in sys.stdin:
	objid,header,seq = line.rstrip("\n").split("\t")
	if(objid!="fasta"):
		raise Excpetion("Invalid input stream, must be fasta-object")
	if(args.upper):
		seq=seq.upper()
	topr=[objid,header,seq]
	print("\t".join(topr))
