
def hamming_distance(file):
    """Calculates Hamming Distance of two strings of equal len, from a txt file."""

    with open(file, "r") as f:
        dna = (f.read()).split()

    i = 0
    hamming_dist = 0
    for d in dna[0]:

        if dna[0][i] != dna[1][i]:
            #print(dna[0][i], dna[1][i])
            hamming_dist +=1

        i +=1
    return print(hamming_dist)


hamming_distance("DNA_Count_point_mutants")

