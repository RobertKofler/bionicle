#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse
prog = re.compile(r"(\d+)([MISDHN])")


class FastaReader:
	"""
	A light-weight fasta reader;
	returns a tuple (header, sequence)
	
	"""
	def __init__(self,fh):
		self.__filehandle=fh
		self.__prevheader=None

	def __iter__(self):
		return self
	
	def close(self):
		self.__filehandle.close()
	
	def __next__(self):
		return self.next()
	
	def next(self):
		line=""
		header=self.__prevheader
		seq=""
		while(1):
			line=self.__filehandle.readline()
			if line=="":					# file is empty
				if(header is not None):
					self.__prevheader=None		# return last sequence
					return (header,seq)
				else:
					raise StopIteration		# file empty and no last sequence -> STOP
			line=line.rstrip("\n")				# somethin is in the file
			if(line.startswith(">")):			# we have a header
				line=line.lstrip(">")
				if(header is None):			# if it is the first header just set the name of the header
					header=line
				else:
					self.__prevheader=line	# if it is any other header, set the previous to the current and return the sequence
					return(header,seq)
			else:
				seq+=line				# normal line, add to sequence


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
#parser.add_argument('--fasta', type=str, default=None,dest="fasta", required=True, help="A fasta file")
args,unknown = parser.parse_known_args()
fh=None
if(len(unknown)>0):
	fh=open(unknown[0])
else:
	fh=sys.stdin

for header,seq in FastaReader(fh):
	
	if " " in header:
		header=header.split(" ")[0]
	topr=["fasta",header,seq]
	print("\t".join(topr))
