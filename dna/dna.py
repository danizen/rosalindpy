import argparse
from os.path import basename, dirname, join


parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('datafile')

opts = parser.parse_args()


sequence = None
with open(opts.datafile, 'r') as f:
    sequence = f.read()

counters = { 'A':  0, 'C':  0, 'G':  0, 'T':  0 };

for c in sequence:
    if c in counters: 
        counters[c] += 1
    
print("%d %d %d %d" % (counters['A'], counters['C'], counters['G'], counters['T']))

