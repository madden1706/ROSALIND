# Given: Three positive integers k, m, and n, representing a population containing
# k+m+n organisms: k individuals are homozygous dominant for a factor, m are
# heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce
# an individual possessing a dominant allele (and thus displaying the dominant
# phenotype). Assume that any two organisms can mate.

from itertools import product
from scipy.special import comb

def mendel(K, M, N):
    """"""
    all = sum([K, M, N])

    combos = product(["k","m","n"], repeat=2)
    #combos = comb([k, m, n], 2)
    for i in combos:
        print(i)

    # 2/8 *

    #Probabilities of individual producing dominant allele offspring.

    k_k = 1

    k_m = 1

    k_n = 1

    m_m = 0.75

    m_n = 0.5

    n_n = 0

    #Weigth probabilities



mendel(2, 2, 2) # 0.78333