import argparse
from os.path import basename, dirname, join
import io



start = 'AUG'

codon2rna_map = {
    'UUU': 'F',
    'UUC': 'F',
    'UUA': 'L',
    'UUG': 'L',
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',
    'UAU': 'Y',
    'UAC': 'Y',
    'UAA': None,
    'UAG': None,
    'UGU': 'C',
    'UGC': 'C',
    'UGA': None,
    'UGG': 'W',
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'CAU': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGU': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'AUG': 'M',
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'AAU': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGU': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G',
}

rna2codon_map = {}
for k, v in codon2rna_map.items():
    if v not in rna2codon_map:
        rna2codon_map[v] = []
    rna2codon_map[v].append(k)


def guts(sequence):
    # scan the sequence, and find all codons whose value match the 
    # next codon.  We multiply the starting number by the number 
    # of these codons, until we are done.   Then, we multiply one 
    # more time, by the number of stop codons.

    count = 1
    for aa in sequence:
        assert aa in rna2codon_map
        count *= len(rna2codon_map[aa])
        count = count % 1000000
    count *= len(rna2codon_map[None])
    count = count % 1000000
    return count


def main(): 
    parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
    parser.add_argument('datafile')

    opts = parser.parse_args()

    sequence = None
    with open(opts.datafile, 'r') as f:
        sequence = f.read().strip()

    result = guts(sequence)
    print(result)


if __name__ == '__main__':
    main()
