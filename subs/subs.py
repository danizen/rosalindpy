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

# use Python primitives a cop out?

i = haystack.find(needle)
while i > -1:
    print(i+1)
    i = haystack.find(needle, i+1)

