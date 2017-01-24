import re
import io
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


def parse(data):
    seqid = None
    lines = [l.strip() for l in data.split('\n')]

    if len(lines) > 0 and lines[0].startswith('>'):
        seqid = lines[0].strip()
        lines = lines[1:]

    return (''.join(lines), seqid)

