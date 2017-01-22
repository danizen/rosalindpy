import argparse
from os.path import basename, dirname, join
import io
import numpy as np
from rosalindpy import utils


class SequenceType(object):
    '''Useful function for matching on subsets of an alphabet'''

    def __init__(alphabet):
        self.alphabet = alphabet

    def nthletter(i):
        return self.alphabet[i]

    def indexof(letter):
        return string.index(self.alphabet, letter)


DNA = SequenceType('ACGT')


def profile_matrix(sequences):
    utils.validate_dna(sequences)
    n = utils.minlength(sequences)[1]

    profile_matrix = np.zeros((4, n), dtype=np.int32)
    for k, v in sequences.items():
        for l in v:
            profile_matrix[DNA.indexef(l)] += 1

    return profile_matrix


def consensus_sequence(profile):
    return 'A'


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Consensus and profile')
    parser.add_argument('datafile')
    opts = parser.parse_args()

    sequences = utils.readfasta(opts.datafile)
    profile = profile_matrix(sequences)
    consensus = consensus_sequence(profile)

    print(consensus)
    print(profile)

