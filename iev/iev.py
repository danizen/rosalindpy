import argparse
from os.path import basename, dirname, join
import io
import numpy as np


def guts(datafile):
    population_genotypes = np.loadtxt(datafile, dtype=np.int32)
    return str(population_genotypes)


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Expected Offspring')
    parser.add_argument('datafile')
    parser.add_argument('--verbose', '-v', type=int)
    opts = parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=opts.verbose)

    expectation = guts(opts.datafile)
    print(expectation)


if __name__ == '__main__':
    main()

