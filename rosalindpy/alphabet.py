import string


class RestrictedAlphabet(object):
    '''Abstract alphabet based on restricted sequence of unicode'''

    def __init__(self, alphabet, meta=None):
        self.alphabet = str(alphabet)
        self.metachars = str(meta) if meta else ''

    def pos2letter(self, i):
        return self.alphabet[i]

    def letter2pos(self, letter):
        return self.alphabet.index(letter)

    def isvalid(self, string_in_alphabet, strict=False):
        for a in string_in_alphabet:
            if a not in self.alphabet:
                if strict:
                    return False
                elif a not in self.metachars:
                    return False 
        return True


DNA = RestrictedAlphabet('ACGT', meta='-')

RNA = RestrictedAlphabet('ACGU', meta='-')

