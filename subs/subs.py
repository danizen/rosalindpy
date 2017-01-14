import argparse
from os.path import basename, dirname, join
import io

parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('datafile')

opts = parser.parse_args()

f = open(opts.datafile, 'r')
haystack = f.readline().strip()
needle = f.readline().strip()

print('haystack = %s' % haystack)
print('needle = %s' % needle)

# use Python primitives a cop out?
