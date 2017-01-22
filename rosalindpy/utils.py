import re
from .errors import *

def readfasta(datafile):
    sequences = {}
    lastseq = None

    with open(datafile, 'r') as f:
        for line in f.readlines():
            sequence = line.strip()
            if sequence.startswith('>'):
                lastseq = sequence[1:].strip()
                sequences[lastseq] = ''
            else:
                sequences[lastseq] += sequence

    return sequences


def __validate_sequences(sequences, validate_func):
    if isinstance(sequences, str):
        validate_func(sequences)
    elif isinstance(sequences, dict):
        for k, v in sequences.items():
            validate_func(v)
    else:
        for v in sequences:
            validate_func(v)
    

def __validate_dna(sequence):
    '''Validate a DNA string'''
    if re.fullmatch(r'[AGCT]+', sequence) is None:
        raise DnaSequenceError()


def validate_dna(sequences):
    '''Validate a DNA string, dict, or iterable'''
    __validate_sequences(sequences, __validate_dna)


def __validate_rna(sequence):
    '''Validate an RNA string'''
    if re.fullmatch(r'[AGCU]+', sequence) is None:
        raise RnaSequenceError()


def validate_rna(sequences):
    '''Validate an RNA string, dict, or iterable'''
    __validate_sequences(sequences, __validate_rna)


def minlength(sequences):
    bestk = None
    bestlen = float('inf')

    for k, v in sequences.items():
        if len(v) < bestlen:
            bestlen = len(v)
            bestk = k

    return (bestk, bestlen)

