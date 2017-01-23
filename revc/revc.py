import argparse
from os.path import basename, dirname, join
import io
from rosalindpy.alphabet import DNA


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__),
                                     description='Reverse complement')
    parser.add_argument('datafile')

    opts = parser.parse_args()

    sequence = None
    with open(opts.datafile, 'r') as f:
        sequence = f.read().strip()

    seqcomplement = DNA.reverse_complement(sequence)
    print(seqcomplement)
    

if __name__ == '__main__':
    main()
