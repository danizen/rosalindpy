import argparse
from os.path import basename, dirname, join
import io


parser = argparse.ArgumentParser(prog=basename(__file__), description='Fubar')
parser.add_argument('k', type=int)
parser.add_argument('m', type=int)
parser.add_argument('n', type=int)

opts = parser.parse_args()

# k organisms are homozygous for a factor (both chromosomes dominant)
# m organisms are heterozygous for a factor (chromosomes different)
# n oragnisms are homozygous recessize for a factor (both chromosomes recessive)

print('k = %d, m = %d, n = %d' % (opts.k, opts.m, opts.n))

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
