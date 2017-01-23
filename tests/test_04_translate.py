import pytest
from rosalindpy.translate import *


def test_rna2protein():
    rnaseq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    (proteinseq, basepaircount) = rna2protein(rnaseq)
    assert proteinseq == 'MAMAPRTEINSTRING'
    assert basepaircount == len(proteinseq)*3


def test_dna2protein():
    dnaseq = 'ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
    (proteinseq, basepaircount) = dna2protein(dnaseq)
    assert proteinseq == 'MAMAPRTEINSTRING'
    assert basepaircount == len(proteinseq)*3

