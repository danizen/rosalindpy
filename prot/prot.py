import argparse
from os.path import basename, dirname, join
from rosalindpy import translate


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
    parser.add_argument('datafile')

    opts = parser.parse_args()

    sequence = None
    with open(opts.datafile, 'r') as f:
        sequence = f.read().strip()

    protseq = translate.rna2protein(sequence)
    print(protseq)


if __name__ == '__main__':
    main()
