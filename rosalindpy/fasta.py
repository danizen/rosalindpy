import re
from .errors import *


def readsimple(datafile):
    '''
    Read a file in fasta format, representing the result as a simple hash
    '''
    sequences = {}
    lastseq = None

    with open(datafile, 'r') as f:
        for line in f.readlines():
            sequence = line.strip()
            if sequence.startswith('>'):
                lastseq = sequence[1:].strip()
            else:
                if lastseq not in sequences:
                    sequences[lastseq] = ''
                sequences[lastseq] += sequence

    return sequences

