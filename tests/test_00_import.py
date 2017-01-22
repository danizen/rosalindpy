from importlib import import_module


def test_import_errors():
    mod = import_module('rosalindpy.errors')
    assert 'DNASequenceError' in dir(mod)
    assert 'RNASequenceError' in dir(mod)


def test_import_alphabet():
    mod = import_module('rosalindpy.alphabet')
    assert 'RestrictedAlphabet' in dir(mod)
    assert 'DNA' in dir(mod)
    assert 'RNA' in dir(mod)


def test_import_utils():
    mod = import_module('rosalindpy.utils')
    assert 'validate_dna' in dir(mod)
    assert 'validate_rna' in dir(mod)


def test_import_fasta():
    mod = import_module('rosalindpy.fasta')
    assert 'readsimple' in dir(mod)


