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

complement = { 
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A' 
}


for c in sequence[::-1]:
    if c in complement:
        io.write(complement[c])

print(io.getvalue())
    

