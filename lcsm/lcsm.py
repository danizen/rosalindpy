import argparse
from os.path import basename, dirname, join
import io
import numpy as np
import re
import requests

from rosalindpy import fasta
from rosalindpy import utils


def guts(sequences):
    # tricks here:
    #    - maximum match will have a length less than shortest sequence
    #    - So, order sequences shortest to longest
    #    - Build a forest (DAG) data structure for the sequences in this order
    #    - Sequences form the nodes of this forward, with 2-letter sequences at the first layer of the tree, 
    #      and so on.  This can be a hash of hashes.
    #    - As you traverse each subsequent sequence, you can remove any sequence which doesn't match between
    #      the two.
    #    - Take a longest node that has no kids (is a leaf)

    # The hope that this would be O(n) on characters is fleeting.
    # we have to be able to color the nodes.  

    # Maybe we swap graphs. We always build a new graph, copying from the old graph.
    # Anything we cannot copy, we drop after the next sequence.
    return 'NYI'



def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Finding a Protein Motif')
    parser.add_argument('datafile')
    opts = parser.parse_args()

    sequences = fasta.readsimple(opts.datafile)
    common_subseq = guts(sequences)
    print(common_subseq)


if __name__ == '__main__':
    main()
