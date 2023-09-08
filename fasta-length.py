#!/usr/bin/env python
import os
import sys
import inspect
import re
import argparse
import collections





for line in sys.stdin:
	objid,header,seq = line.rstrip("\n").split("\t")
	topr=[header,str(len(seq))]
	print("\t".join(topr))
	
