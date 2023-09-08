#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse


parser = argparse.ArgumentParser(description="""           
Fastq writer:
functions:
format fastq
.. many more possible
""",formatter_class=argparse.RawDescriptionHelpFormatter,
epilog="""
Authors
-------
    Robert Kofler
""")
#parser.add_argument("--min-len", type=int, required=False, dest="minlen", default=None, help="minimum length of read")

args = parser.parse_args()



for line in sys.stdin:
	line=line.rstrip("\n")
	objid,h1,seq,h2,qual = line.split("\t")
	print(h1)
	print(seq)
	print(h2)
	print(qual)