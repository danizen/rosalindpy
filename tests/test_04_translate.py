import pytest
from rosalindpy.translate import *


def test_rna2protein():
    rnaseq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    proteinseq = rna2protein(rnaseq)
    assert proteinseq == 'MAMAPRTEINSTRING'


def test_dna2protein():
    dnaseq = 'ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
    proteinseq = dna2protein(dnaseq)
    assert proteinseq == 'MAMAPRTEINSTRING'


def test_dna_orfs():
    dnaseq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
    frames = open_reading_frames(dnaseq)
    assert len(frames) == 5
    assert 4 in frames
    assert frames[4] == 'M'
    assert -5 in frames
    assert frames[-5] == 'MLLGSFRLIPKETLIQVAGSSPCNLS'
    assert -70 in frames
    assert frames[-70] == 'M'
    assert 24 in frames
    assert frames[24] == 'MGMTPRLGLESLLE'
    assert 30 in frames
    assert frames[30] == 'MTPRLGLESLLE'

