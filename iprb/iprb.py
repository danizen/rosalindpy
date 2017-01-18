import argparse
import numpy as np
from os.path import basename, dirname, join
import io

class Allele(object):
    HOMOZYGOUS = 0
    HETEROZYGOUS = 1
    HOMOZYGOUS_RECESSIVE = 2


    @classmethod
    def all(cls):
        return [cls.HOMOZYGOUS, cls.HETEROZYGOUS, cls.HOMOZYGOUS_RECESSIZE]
        

class Population(object):

    def __init__(self, counts):
        if len(counts) != 3:
            raise Exception('expecting just 3 integers')
        if isinstance(counts, np.ndarray):
            self.counts = counts
        else:
            self.counts = np.array(counts, dtype=np.int64)

    @property
    def total(self):
        return self.counts.sum()

    def probability(self, organism_type):
        return self.counts[organism_type]/self.total

    def take(self, organism_type):
        assert self.counts[organism_type] > 0
        newcounts = self.counts.copy()
        newcounts[organism_type] -= 1
        return Population(newcounts)


class ProbalityTreePath(object):

    def __init__(self, population, probality, allele_mother, allele_father)
        self.probality = probality
        self.allele_mother = allele_mother
        self.allele_father = allele_father

    def hasfeature(self):
        return "F" in self.path


def add_tree_paths(paths, allele_mother, allele_father, probability):
    switch 

# we assume that all organisms are hermaphrodites

# Let Random Variable X := 1st organism's allele
# Let Random Variable Y : 2nd organism's allele
# Let Random Variable Z : offspring's allele
# Let the factor be written D for dominant or d for recessive

# Pr{Z has factor} = Pr{Z == homozygous} + Pr{Z == heterozygous}
# Pr{Z has factor} = 1 - Pr{Z == homozygous recessive}

# Pr{Z == homozygous recessive} 
#                     = Pr{X == homozygous recessive}Pr{Y == homozygous recessive}
#                     + (Pr{X == heterozygous}/2)Pr{Y == homozygous recessive}
#                     + Pr{X == homozygous recessive}(Pr{Y == heterozygous}/2)
#                     + (Pr{X == heterozygous}Pr{Y == heterozygous}/4)

# Pr{X == homozygous} = k/(k+m+n) 
# Pr{X == heterozygous} = m/(k+m+n)
# Pr{X == homozygous recessive} = n/(k+m+n)

# Pr{Y == homozyous}/Pr{X == homozygous} = (k-1)/(k+m+n-1)
# Pr{Y == homozyous}/Pr{X == hetezygous} = k/(k+m+n-1)
# Pr{Y == homozyous)/Pr{X == homozygous recessive} = k/(k+m+n-1)

# Pr{Y == heterozygous}/Pr{X == homozygous} = m/(k+m+n-1)
# Pr{Y == heterozygous}/Pr{X == heterozygous} = (m-1)/(k+m+n-1)
# Pr{Y == heterozygous}/Pr{X == homozygous recessive} = m/(k+m+n-1)

# Pr{Y == homozygous recessive}/Pr{X == homozygous} = n/(k+m+n-1)
# Pr{Y == homozygous recessive}/Pr{X == heterozygous} = n/(k+m+n-1)
# Pr{Y == homozygous recessive}/Pr{X == homozygous recessive} = (n-1)/(k+m+n-1)




# Pr{Y == heteroy

# Pr{1st organim

def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
    parser.add_argument('k', type=int)
    parser.add_argument('m', type=int)
    parser.add_argument('n', type=int)
    parser.add_argument('--verbose', '-v')

    opts = parser.parse_args()

    # k organisms are homozygous for a factor (both chromosomes dominant)
    # m organisms are heterozygous for a factor (chromosomes different)
    # n oragnisms are homozygous recessize for a factor (both chromosomes recessive)

    if opts.verbose:
        print('k = %d, m = %d, n = %d' % (opts.k, opts.m, opts.n)) 


    paths = []

    population = Popuplation([opts.k, opts.m, opts.n])
    for allele_mother in Allele.all():
        probality_mother = population.probability(allele_mother)
        subpopulation = population.take(allele_mother)

        for allele_father in Allele.all():

            probability_father = subpopulation.probability(allele_father)
            probability = probality_mother * probability_father

            add_tree_paths(path, allele_mother, probability_mother, allele_father, probability_father)

    if opts.verbose:
        for path in paths:
            print("path %s 



if __name__ == '__main__':
    main()

