import re
from .errors import *
from .alphabet import DNA, RNA

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


def minlength(sequences):
    bestk = None
    bestlen = float('inf')

    for k, v in sequences.items():
        if len(v) < bestlen:
            bestlen = len(v)
            bestk = k

    return (bestk, bestlen)

