import argparse
from os.path import basename, dirname, join
import io
import numpy as np



class Cohort(object):

    def __init__(self, lifespan, birthrate, initial=1):
        self.lifespan = lifespan
        self.birthrate = birthrate
        self.cohort = np.zeros(self.lifespan, dtype=np.int64)
        self.cohort[0] = initial

    def population(self):
        return self.cohort.sum()

    def age(self):
        newborn = self.cohort[1:].sum() * self.birthrate
        self.cohort = np.roll(self.cohort, 1)
        self.cohort[0] = newborn


def main():
    parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
    parser.add_argument('months', type=int)
    parser.add_argument('lifespan', type=int)
    parser.add_argument('--birthrate', type=int, default=1)

    opts = parser.parse_args()

    print('months = %d' % opts.months)
    print('lifespan = %d' % opts.lifespan)

    cohort = Cohort(opts.lifespan, opts.birthrate)


    for i in range(0, opts.months):
        print(cohort.population())
        cohort.age()


if __name__ == '__main__':
    main()

