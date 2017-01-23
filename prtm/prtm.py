import argparse
from os.path import basename, dirname, join
import io
import numpy as np

from rosalindpy import fasta
from rosalindpy import utils


def guts(datafile):
    sequences = fasta.readsimple(datafile)

    assert len(sequences) == 1

    protein_mass = None
    for k, v in sequences.items():
        protein_mass = utils.protein_mass(v)

    return protein_mass


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Open Reading Frames')
    parser.add_argument('datafile', help='In fasta format')
    opts = parser.parse_args()

    protein_mass = guts(opts.datafile)

    print('%.3f' % protein_mass)


if __name__ == '__main__':
    main()
