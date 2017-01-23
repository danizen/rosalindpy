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
    assert len(frames) == 4
    assert 'M' in frames
    assert 'MLLGSFRLIPKETLIQVAGSSPCNLS' in frames
    assert 'MGMTPRLGLESLLE' in frames
    assert 'MTPRLGLESLLE' in frames

