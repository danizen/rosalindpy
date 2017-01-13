import argparse
from os.path import basename, dirname, join
import io


parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('datafile')

opts = parser.parse_args()

sequences = {}
lastseq = None

with open(opts.datafile, 'r') as f:
    for line in f.readlines():
        sequence = line.strip()
        if sequence.startswith('>'):
            lastseq = sequence[1:]
            sequences[lastseq] = ''
        else:
            sequences[lastseq] += sequence
        
best_gc = 0.0
best_name = None

for name, sequence in sequences.items():
    gc = 100.0 * (sequence.count('C') + sequence.count('G'))/len(sequence)
    if gc > best_gc:
        best_gc = gc
        best_name = name

print(best_name)
print('%f' % best_gc)

