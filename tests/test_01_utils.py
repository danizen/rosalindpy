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


