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

