import argparse
from os.path import basename, dirname, join
import io
import re

parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('datafile')
parser.add_argument('--verbose', '-v')

opts = parser.parse_args()

f = open(opts.datafile, 'r')
haystack = f.readline().strip()
needle = f.readline().strip()

if opts.verbose:
    print('haystack = %s' % haystack)
    print('needle = %s' % needle)

# subs.py uses Knuth-Morris-Pratt as a cop out
# the objective of subs2 is to implement something a bit more ambitious

i = haystack.find(needle)
while i > -1:
    print(i+1)
    i = haystack.find(needle, i+1)

