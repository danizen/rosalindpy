import pytest
from rosalindpy import utils
from rosalindpy.errors import *


def test_validate_dna_ok():
    sequence = 'ATCCAGCT'
    utils.validate_dna(sequence)


def test_validate_dna_dict_ok():
    sequences = { '1': 'ATCCAGCT', '2': 'TTGGAACT' }
    utils.validate_dna( sequences )


def test_validate_dna_array_ok():
    sequences = [ 'ATCCAGCT', 'TTGGAACT' ]
    utils.validate_dna( sequences )


def test_validate_dna_error():
    sequences = [ 'ATCCAGCT', 'TTGGAACQ' ]
    with pytest.raises(DNASequenceError):
        utils.validate_dna( sequences )


def test_protein_mass():
    sequence = 'SKADYEK'
    result = '%.3f' % utils.protein_mass(sequence)
    assert result == '821.392'


def test_basic_motif():
    motif = utils.Motif('N{P}[ST]{P}')
    s = 'PPPPNNTTGGGG'
    assert motif.matches(s)
    locs = [l for l in motif.locations(s)]
    assert len(locs) == 2
    assert locs[0] == (4,8)
    assert locs[1] == (5,9)

