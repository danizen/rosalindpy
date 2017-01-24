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

    Process first sequence into suffix tree

    
    Loop invariant:
        tree := sequences present in all sequences so far processed

    For each subsequent sequence, 
        do the stuff
        
    tree = tree of sequences in all 

    # The hope that this would be O(n) on characters is fleeting.  we have to
    # be able to color the nodes.  

    # Maybe we swap graphs. We always build a new graph, copying from the old
    # graph.  Anything we cannot copy, we drop after the next sequence.

    # NOTE: The design above is a classic algorithm based on suffix trees, it
    # is almost equivalent to say that the edges are subsequent characters.
    # This permits more than one character at a time. There is also a dynamic
    # programming solution, but I don't get it yet.

    # There are python modules that implement this already -
    # https://github.com/ptrus/suffix-trees for example.  Worthwhile to program
    # it myself?   Biopython probably has this somewhere, too.

    # I don't see how the DP solution will generalize to N such strings, but I
    # do see how the suffix tree version will do so.

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
