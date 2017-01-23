import io
from .alphabet import DNA

RNA_START_CODON = 'AUG'

RNA_CODON2AA_MAP = {
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

DNA_START_CODON = 'ATG'

DNA_CODON2AA_MAP = {
    'TTT': 'F',
    'TTC': 'F',
    'TTA': 'L',
    'TTG': 'L',
    'TCT': 'S',
    'TCC': 'S',
    'TCA': 'S',
    'TCG': 'S',
    'TAT': 'Y',
    'TAC': 'Y',
    'TAA': None,
    'TAG': None,
    'TGT': 'C',
    'TGC': 'C',
    'TGA': None,
    'TGG': 'W',
    'CTT': 'L',
    'CTC': 'L',
    'CTA': 'L',
    'CTG': 'L',
    'CCT': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'CAT': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGT': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'ATT': 'I',
    'ATC': 'I',
    'ATA': 'I',
    'ATG': 'M',
    'ACT': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'AAT': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGT': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GTT': 'V',
    'GTC': 'V',
    'GTA': 'V',
    'GTG': 'V',
    'GCT': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAT': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGT': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G',
}


def __codonmap2protein(sequence, pos, codonmap):
    protseq = io.StringIO()

    # scan the sequence in sections of three, 
    while pos + 3 <= len(sequence):
        seq = sequence[pos:pos+3]
        aa = codonmap[seq]
        if aa is None:
            return protseq.getvalue()
        protseq.write(aa)
        pos += 3

    return None


def rna2protein(sequence, pos=0):
    return __codonmap2protein(sequence, pos, RNA_CODON2AA_MAP)


def dna2protein(sequence, pos=0):
    return __codonmap2protein(sequence, pos, DNA_CODON2AA_MAP)


def open_reading_frames(sequence):

    frames = []

    pos = 0
    while pos < len(sequence):
        pos = sequence.find(DNA_START_CODON, pos)
        if pos < 0:
            break
        protein_seq = dna2protein(sequence, pos)
        if protein_seq is None:
            break
        if not protein_seq in frames:
            frames.append(protein_seq)
        pos += 3

    seqc = DNA.reverse_complement(sequence)
    pos = 0
    while pos < len(seqc):
        pos = seqc.find(DNA_START_CODON, pos)
        if pos < 0:
            break
        protein_seq = dna2protein(seqc, pos)
        if protein_seq is None:
            break
        if not protein_seq in frames:
            frames.append(protein_seq)
        pos += 3

    return frames

