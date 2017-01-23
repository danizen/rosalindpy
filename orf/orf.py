import argparse
from os.path import basename, dirname, join
import io
import numpy as np
import logging

from rosalindpy import translate
from rosalindpy import fasta
from rosalindpy import utils


def guts(datafile):
    sequences = fasta.readsimple(datafile)

    assert len(sequences) == 1
    utils.validate_dna(sequences)

    frames = None
    for k, v in sequences.items():
        frames = translate.open_reading_frames(v)

    return frames


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Open Reading Frames')
    parser.add_argument('datafile')
    parser.add_argument('--verbose', '-v', metavar='LEVEL', type=int)
    opts = parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=opts.verbose)

    frames = guts(opts.datafile)
    if opts.verbose:
        for k, v in frames.items():
            print('at %d: %s' % (k, v))
    else:
        uniqframes = set(frames.values())
        for f in uniqframes:
            print(f)

if __name__ == '__main__':
    main()
