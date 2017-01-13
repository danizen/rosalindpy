import argparse
from os.path import basename, dirname, join
import io


parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('months', type=int)
parser.add_argument('offspring', type=int)

opts = parser.parse_args()

print('months = %d' % opts.months)
print('offspring = %d' % opts.offspring)

breeding_pairs = 1
young_pairs = 0

print(1)
print(1)

for i in range(2, opts.months):

    pairs_born = breeding_pairs * opts.offspring
    breeding_pairs += young_pairs
    young_pairs = pairs_born

    print(str(breeding_pairs + young_pairs))

