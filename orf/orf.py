import argparse
from os.path import basename, dirname, join
import io
import numpy as np
import logging

from rosalindpy import translate
from rosalindpy import fasta
from rosalindpy import utils

from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import six_frame_translations

logger = logging.getLogger(__name__)


def guts(datafile):
    sequences = fasta.readsimple(datafile)

    assert len(sequences) == 1
    utils.validate_dna(sequences)

    frames = None
    for k, v in sequences.items():
        frames = translate.open_reading_frames(v)

    return frames


def guts_biopython(datafile):
    seqrec = SeqIO.read(datafile, 'fasta', alphabet=IUPAC.unambiguous_dna)
    seq = seqrec.seq
    logger.info('sequence %s' % str(seq))

    print(six_frame_translations(seq))

    nbp = len(seq)

    frames = {}
    pos = seq.find('ATG')
    while (pos > 0):
        framlen = nbp - pos 
        framlen -= framlen % 3
        subseq = seq[pos:framlen]
        prot = subseq.translate(to_stop=True)
        frames[pos] = prot
        pos = seq.find('ATG', pos+1)

    revseq = seq.reverse_complement()
    logger.info('reverse complement %s' % str(revseq))
    pos = revseq.find('ATG')
    while (pos > 0):
        framlen = nbp - pos 
        framlen -= framlen % 3
        subseq = revseq[pos:framlen]
        prot = subseq.translate(to_stop=True)
        frames[-1 * pos] = prot
        pos = revseq.find('ATG', pos+1)

    return frames


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), 
                                     description='Open Reading Frames')
    parser.add_argument('datafile', help='In fasta format')
    parser.add_argument('--verbose', '-v', metavar='LEVEL', type=int,
                        help='Configure logging to this level of output')
    parser.add_argument('--biopython', default=False, action='store_true',
                        help='Use biopython to check our logic')
    opts = parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=opts.verbose)

    if opts.biopython:
        frames = guts_biopython(opts.datafile)
    else:
        frames = guts(opts.datafile)

    if opts.verbose:
        for k in sorted(frames.keys()):
            v = frames[k]
            print('at %d: %s' % (k, v))
    else:
        uniqframes = set()
        for k in sorted(frames.keys()):
            v = frames[k]
            if v not in uniqframes:
                uniqframes.add(v)
                print(v)

if __name__ == '__main__':
    main()
