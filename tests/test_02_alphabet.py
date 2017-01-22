import pytest
from rosalindpy.alphabet import *
from rosalindpy.errors import *


def test_dna_isvalid():
    assert DNA.isvalid('ATCCAGCT')

def test_dna_isvalid_notstrictk():
    assert DNA.isvalid('ATCC-AGCT', strict=False)

def test_dna_not_isvalid():
    assert not DNA.isvalid('ATCCAQGCT')

def test_dna_not_isvalid_notstrict():
    assert not DNA.isvalid('ATCC-*AGCT', strict=False)

def test_dna_letter2pos():
    assert DNA.letter2pos('A') == 0
    assert DNA.letter2pos('C') == 1
    assert DNA.letter2pos('G') == 2
    assert DNA.letter2pos('T') == 3

def test_dna_pos2letter():
    assert DNA.pos2letter(0) == 'A'
    assert DNA.pos2letter(1) == 'C'
    assert DNA.pos2letter(2) == 'G'
    assert DNA.pos2letter(3) == 'T'

def test_dna_len():
    assert len(DNA) == 4

def test_rna_isvalid():
    assert RNA.isvalid('AUCCAGCU')

def test_rna_isvalid_notstrictk():
    assert RNA.isvalid('AUCC-AGCU', strict=False)

def test_rna_not_isvalid():
    assert not RNA.isvalid('ATCCAGCT')

def test_rna_not_isvalid_notstrict():
    assert not RNA.isvalid('AUCC-AGCU*', strict=False)

def test_rna_letter2pos():
    assert RNA.letter2pos('A') == 0
    assert RNA.letter2pos('C') == 1
    assert RNA.letter2pos('G') == 2
    assert RNA.letter2pos('U') == 3

def test_rna_pos2letter():
    assert RNA.pos2letter(0) == 'A'
    assert RNA.pos2letter(1) == 'C'
    assert RNA.pos2letter(2) == 'G'
    assert RNA.pos2letter(3) == 'U'

def test_rna_len():
    assert len(RNA) == 4
