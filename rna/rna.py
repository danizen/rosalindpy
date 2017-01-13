import argparse
from os.path import basename, dirname, join
import io


parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('datafile')

opts = parser.parse_args()


sequence = None
with open(opts.datafile, 'r') as f:
    sequence = f.read().strip()

io = io.StringIO()

trans = { 'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U' }


for c in sequence:
    if c in trans:
        io.write(trans[c])

print(io.getvalue())
    

