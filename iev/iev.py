import argparse
from os.path import basename, dirname, join
import io


def guts(datafile):
    return 'Doable, but tedious'


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

