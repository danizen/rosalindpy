from importlib import import_module


def test_import_errors():
    mod = import_module('rosalindpy.errors')


def test_import_utils():
    mod = import_module('rosalindpy.utils')

