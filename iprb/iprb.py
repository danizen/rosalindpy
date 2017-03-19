import argparse
import numpy as np
from os.path import basename, dirname, join
import io
from rosalindpy.population import Genotype as Allele


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
        newcounts = self.counts.copy()
        if self.counts[organism_type] > 0:
            newcounts[organism_type] -= 1
        return Population(newcounts)


# Hard to fix - these are business rules.   We can improve by accumulating probability
# of child alleles to some matrix.

def accumulate_child_probability(children, probability, allele_mother, allele_father):

    if allele_mother == Allele.HOMOZYGOUS:
        if allele_father == Allele.HOMOZYGOUS:
            children[ Allele.HOMOZYGOUS ] += probability
        elif allele_father == Allele.HOMOZYGOUS_RECESSIVE:
            children[ Allele.HETEROZYGOUS ] += probability
        else:
            children[ Allele.HOMOZYGOUS ] += probability / 2
            children[ Allele.HETEROZYGOUS ] += probability / 2
    elif allele_mother == Allele.HOMOZYGOUS_RECESSIVE:
        if allele_father == Allele.HOMOZYGOUS:
            children[ Allele.HETEROZYGOUS ] += probability
        elif allele_father == Allele.HOMOZYGOUS_RECESSIVE:
            children[ Allele.HOMOZYGOUS_RECESSIVE ] += probability
        else:
            children[ Allele.HETEROZYGOUS ] += probability / 2
            children[ Allele.HOMOZYGOUS_RECESSIVE ] += probability / 2
    else:
        if allele_father == Allele.HOMOZYGOUS:
            children[ Allele.HOMOZYGOUS ] += probability / 2
            children[ Allele.HETEROZYGOUS ] += probability / 2
        elif allele_father == Allele.HOMOZYGOUS_RECESSIVE:
            children[ Allele.HETEROZYGOUS ] += probability / 2
            children[ Allele.HOMOZYGOUS_RECESSIVE ] += probability / 2
        else:
            # both parents are heterozygous
            children[ Allele.HOMOZYGOUS ] += probability / 4
            children[ Allele.HOMOZYGOUS_RECESSIVE ] += probability / 4
            children[ Allele.HETEROZYGOUS ] += probability / 2



def guts(k, m, n, verbose=True):

    # k organisms are homozygous for a factor (both chromosomes dominant)
    # m organisms are heterozygous for a factor (chromosomes different)
    # n oragnisms are homozygous recessize for a factor (both chromosomes recessive)
    # we assume that all organisms are hermaphrodites

    if verbose:
        print('k = %d, m = %d, n = %d' % (k, m, n)) 


    # chances of children of each type
    children = np.zeros(3, dtype=np.float64)

    # population counts, and calculation of probability of member of each type
    population = Population([k, m, n])

    # calculate chances of each outcome (child allele) in decision tree
    for allele_mother in Allele.all():
        probality_mother = population.probability(allele_mother)
        subpopulation = population.take(allele_mother)

        for allele_father in Allele.all():

            probability_father = subpopulation.probability(allele_father)
            probability = probality_mother * probability_father

            accumulate_child_probability(children, probability, allele_mother, allele_father)

    if verbose:
        print("chance child is homozygous = %lf" % children[Allele.HOMOZYGOUS])
        print("chance child is heterozygous = %lf" % children[Allele.HETEROZYGOUS])
        print("chance child is homozygous recessive = %lf" % children[Allele.HOMOZYGOUS_RECESSIVE])


    return children[Allele.HOMOZYGOUS] + children[Allele.HETEROZYGOUS]


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
    parser.add_argument('k', type=int)
    parser.add_argument('m', type=int)
    parser.add_argument('n', type=int)
    parser.add_argument('--verbose', '-v')

    opts = parser.parse_args()

    chance_has_feature = guts(opts.k, opts.m, opts.n, opts.verbose)
    print("%.5lf" % chance_has_feature)


if __name__ == '__main__':
    main()

