import re
from .errors import *
from .alphabet import DNA, RNA, Protein


MONOISOTOPIC_MASS_MAP = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}


class Motif(object):

    @staticmethod
    def compile(pattern):
        rexpr = r''
        for c in pattern:
            if c == '{':
                rexpr += r'[^'
            elif c == '}':
                rexpr += r']'
            else:
                rexpr += c
        return re.compile(rexpr)
        
    def __init__(self, pattern):
        self.pattern = pattern
        self.__expr = Motif.compile(pattern)

    def __repr__(self):
        return "Motif('%s')" % self.pattern

    def matches(self, sequence):
        return self.__expr.search(sequence)

    def locations(self, sequence):
        m = self.__expr.search(sequence)
        while m is not None:
            yield (m.start(), m.end())
            m = self.__expr.search(sequence, m.start()+1)


def __validate_sequences(theinput, thealphabet, theexception):
    if isinstance(theinput, str):
        if not thealphabet.isvalid(theinput):
            raise theexception()
    elif isinstance(theinput, dict):
        for k, v in theinput.items():
            __validate_sequences(v, thealphabet, theexception)
    else:
        for v in theinput:
            __validate_sequences(v, thealphabet, theexception)
    

def validate_dna(sequences):
    '''Validate a DNA string, dict, or iterable'''
    __validate_sequences(sequences, DNA, DNASequenceError)


def validate_rna(sequences):
    '''Validate an RNA string, dict, or iterable'''
    __validate_sequences(sequences, RNA, RNASequenceError)


def validate_protein(sequences):
    __validate_sequences(sequences, Protein, ProteinSequenceError)


def minlength(sequences):
    bestk = None
    bestlen = float('inf')

    for k, v in sequences.items():
        if len(v) < bestlen:
            bestlen = len(v)
            bestk = k

    return (bestk, bestlen)


def protein_mass(sequence):
    validate_protein(sequence)
    total = 0.0
    for i in sequence:
        assert i in MONOISOTOPIC_MASS_MAP
        total += MONOISOTOPIC_MASS_MAP[i]
    return total

