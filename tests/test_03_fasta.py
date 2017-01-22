import io
import os
from tempfile import mkstemp
import pytest

from rosalindpy import fasta


goodfasta_lines = [
    'GGGCAACT',
    '>Rosalind_1',
    'ATCCAGCT',
    '>  Rosalind_2  ',
    'GGGCAACT\t',
    ' ATGGATCT',
]

@pytest.fixture(scope='module')
def goodfasta(request):
    fh, fnm = mkstemp(prefix='pyt_')
    fh = io.open(fh, mode='w')
    for line in goodfasta_lines:
        fh.write(line)
        fh.write('\n')
    fh.close()
    yield fnm 
    os.remove(fnm)


def test_fasta_readsimple(goodfasta):
    sequences = fasta.readsimple(goodfasta)
    assert None in sequences
    assert 'Rosalind_1' in sequences
    assert 'Rosalind_2' in sequences
    assert len(sequences) == 3

    assert sequences[None] == 'GGGCAACT'
    assert sequences['Rosalind_1'] == 'ATCCAGCT'
    assert sequences['Rosalind_2'] == 'GGGCAACTATGGATCT'

