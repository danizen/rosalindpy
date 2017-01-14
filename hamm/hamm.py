#
# Problem of counting point mutations is much easier than Levinsheim
# distances, but is the problem really that simple in real life?
#
import argparse
from os.path import basename, dirname, join
import io


parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('datafile')

opts = parser.parse_args()


f = open(opts.datafile, 'r') 
seq1 = f.readline().strip()
seq2 = f.readline().strip()

assert len(seq1) == len(seq2)

# This is brute force
count = 0
for i in range(0, len(seq1)):
    if seq1[i] != seq2[i]:
        count += 1

print(count)
    

# NOTE: tempting to start representing genetic sequence codes A, G, C, T 
# with bits, so that complements are bitwise complements ~C = G. ~A = T.
# Maybe 11/00 and 10/01 are pairs.
# 
# Can we transform this into binary hamming distance.


# NOTE 2: Assuming that mutations are rare, then we can divide the sequence
# into groups, and test recursively which contain mutations.  Ultimately,
# we have to compare short sequences, but not all of them.  We can use hashes
# are plain string equality to test sub-sequencies.
