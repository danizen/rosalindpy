import argparse
from os.path import basename, dirname, join
import io
import numpy as np

from rosalindpy import utils
from rosalindpy.alphabet import DNA
from rosalindpy import fasta


def profile_matrix(sequences):
    utils.validate_dna(sequences)
    n = utils.minlength(sequences)[1]

    profile_matrix = np.zeros( (len(DNA), n), dtype=np.int64 )
    for k, v in sequences.items():
        for pos in range(0, n):
            nucleutide = DNA.letter2pos(v[pos])
            profile_matrix[nucleutide, pos] += 1

    return profile_matrix


def consensus_sequence(profile):
    seq = io.StringIO()
    for pos in profile.argmax(axis=0):
        seq.write(DNA.pos2letter(pos))
    return seq.getvalue()


def guts(datafile):
    sequences = fasta.readsimple(datafile)
    profile = profile_matrix(sequences)
    consensus = consensus_sequence(profile)
    return (profile, consensus)


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Consensus and profile')
    parser.add_argument('datafile')
    opts = parser.parse_args()

    profile, consensus = guts(opts.datafile)

    print(consensus)

    for letter in DNA.alphabet:
        row_num = DNA.letter2pos(letter)
        row = profile[row_num]
        rowstr = ' '.join([str(n) for n in row])
        print('%s: %s' % (letter, rowstr))

if __name__ == '__main__':
    main()
