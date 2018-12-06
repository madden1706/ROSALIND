

def offspring_calc(data):
    # Probabilities that a dominant allele is present in offspring.
    prob_dominant = [1, 1, 1, 0.75, 0.5, 0]
    offspring = [a*b for a,b in zip(prob_dominant, data)]
    # Adjust total for two offspring.
    offspring = sum(offspring * 2)
    print(offspring)


sample = [1, 0, 0, 1, 0, 1]
test = [17934, 17446, 18046, 18905, 19032, 19586]

offspring_calc(sample)
offspring_calc(test)


# 1 = 1
# 2 = 1
# 3 = 1
# 4 = 0.75
# 5 = 0.5
# 6 = 0
