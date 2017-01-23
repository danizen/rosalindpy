
class Genotype(object):
    HOMOZYGOUS = 0
    HETEROZYGOUS = 1
    HOMOZYGOUS_RECESSIVE = 2

    @classmethod
    def all(cls):
        return [cls.HOMOZYGOUS, cls.HETEROZYGOUS, cls.HOMOZYGOUS_RECESSIVE]

    @classmethod
    def hasfeature(cls, allele_type):
        return False if allele_type == cls.HOMOZYGOUS_RECESSIVE else True


class Couple(object):

    def __init__(self, genotypes):
        self.genotypes = genotypes

    def probability_of_genotype(genotype):
        return 0.0

