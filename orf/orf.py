import argparse
from os.path import basename, dirname, join
import io
import numpy as np

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
    opts = parser.parse_args()

    frames = guts(opts.datafile)

    for f in frames:
        print(f)

if __name__ == '__main__':
    main()
