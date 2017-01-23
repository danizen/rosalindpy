import string
import io


class RestrictedAlphabet(object):
    '''Abstract alphabet based on restricted sequence of unicode'''

    def __init__(self, alphabet, meta=None):
        self.alphabet = str(alphabet)
        self.metachars = str(meta) if meta else ''

    def pos2letter(self, i):
        return self.alphabet[i]

    def letter2pos(self, letter):
        return self.alphabet.index(letter)

    def __len__(self):
        return len(self.alphabet)

    def isvalid(self, string_in_alphabet, strict=False):
        for a in string_in_alphabet:
            if a not in self.alphabet:
                if strict:
                    return False
                elif a not in self.metachars:
                    return False 
        return True


class DNAAlphabet(RestrictedAlphabet):

    __complement_map = { 
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A' 
    }

    def __init__(self):
        super().__init__('ACGT', meta='-')

    def reverse_complement(self, sequence):
        seqc = io.StringIO()
        for c in sequence[::-1]:
            if c in self.__complement_map:
                seqc.write(self.__complement_map[c])
        return seqc.getvalue()



DNA = DNAAlphabet()

RNA = RestrictedAlphabet('ACGU', meta='-')

Protein = RestrictedAlphabet('ACDEFGHIKLMNPQRSTVWY', meta='-*')

