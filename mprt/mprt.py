import argparse
from os.path import basename, dirname, join
import io
import numpy as np
import re
import requests

from rosalindpy import fasta
from rosalindpy import utils


def guts(motif_pattern, uniprot_id):
    # tricks here:
    #    - retrieve the uniprot_id in fasta format, and read it following redirects.
    #    - compile the motif into a regular expression, following the {P} means any letter except P,
    #      e.g., [^P]
    #    - run the regular expression against it

    url = 'http://uniprot.org/uniprot/%s.fasta' % uniprot_id
    r = requests.get(url)
    data = r.content.decode('utf-8')
    seq, sid = fasta.parse(data)

    motif = utils.Motif(motif_pattern)
    if motif.matches(seq):
        print(uniprot_id)
        matches_start = [str(s+1) for s,e in motif.locations(seq)]
        print(' '.join(matches_start))


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Finding a Protein Motif')
    parser.add_argument('--motif', default=r'N{P}[ST]{P}')
    parser.add_argument('datafile')
    opts = parser.parse_args()

    with open(opts.datafile, 'r') as f:
        for line in f.readlines():
            guts(opts.motif, line.strip())


if __name__ == '__main__':
    main()
