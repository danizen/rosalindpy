class DNASequenceError(Exception):
    '''Not a valid DNA sequence'''
    pass


class RNASequenceError(Exception):
    '''Not a valid RNA sequence'''
    pass


class AminoAcidSequenceError(Exception):
    '''Not a valid Amino Acid sequence'''
    pass


class FastaError(Exception):
    '''Invalid Fasta file'''
    pass

