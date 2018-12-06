# Given: Three positive integers k, m, and n, representing a population containing
# k+m+n organisms: k individuals are homozygous dominant for a factor, m are
# heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce
# an individual possessing a dominant allele (and thus displaying the dominant
# phenotype). Assume that any two organisms can mate.

from itertools import product
from scipy.special import comb


def mendel(k, m, n):

    total_pop = k + m + n

    # dict of probs for getting a first individual.
    first_individual = {"k": k/total_pop, "m": m/total_pop, "n": n/total_pop}

    total_pop2 = total_pop -1

    # dict of probs for getting a second individual.
    second_individual = {
    "k": {"k": (k - 1)/total_pop2, "m": m/total_pop2, "n": n/total_pop2},
    "m": {"k": k/total_pop2, "m": (m - 1)/total_pop2, "n": n/total_pop2},
    "n": {"k": k/total_pop2, "m": m/total_pop2, "n": (n - 1)/total_pop2},
    }

    # print(first_individual)
    # print(first_k)

    combos = product(["k", "m", "n"], repeat=2)
    prob_dict = {}

    # prob of getting a pair of individuals returned for the starting pop.
    for i in combos:
        # print(i)
        one = first_individual[i[0]]

        if i[1] == "k":
            two = second_individual[i[0]]["k"]
        elif i[1] == "m":
            two = second_individual[i[0]]["m"]
        elif i[1] == "n":
            two = second_individual[i[0]]["n"]

        prob = one * two
        prob_dict[i] = prob

    # print("prob_dict", prob_dict)
    # print(sum(prob_dict.values()))

    # weighted prob of getting a dominant allele phenotype.
    prob_dict_weighted = prob_dict


    for i in prob_dict_weighted:
        if "k" in i:
            prob_dict_weighted[i] = prob_dict_weighted[i] * 1  # if contains "k" prob = 1

        elif i == ("n", "n"):
            prob_dict_weighted[i] = prob_dict_weighted[i] * 0  # if nn prob = 0

        elif i == ("m", "n"):
            prob_dict_weighted[i] = prob_dict_weighted[i] * 0.5   # if mn prob = 0.5

        elif i == ("n", "m"):
            prob_dict_weighted[i] = prob_dict_weighted[i] * 0.5

        elif i == ("m", "m"):
            prob_dict_weighted[i] = prob_dict_weighted[i] * 0.75  # if mm prob = 0.75

    # print(prob_dict_weighted)
    print("Probability of phenotype:", sum(prob_dict_weighted.values()))


mendel(2, 2, 2)  # 0.78333

mendel(15, 19, 27)

