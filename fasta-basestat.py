#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse
import collections





for line in sys.stdin:
	basehash=collections.defaultdict(lambda:0)
	
	objid,header,seq = line.rstrip("\n").split("\t")
	for i in list(seq):
		basehash[i]+=1
	print(header)
	for b,c in basehash.items():
		topr=[b,str(c)]
		print("\t".join(topr))
	
