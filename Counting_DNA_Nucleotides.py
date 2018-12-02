#Count each of the bases and give a total for A, C, G and T.

#s = input("What is the DNA sequence?").upper()
#print(dna)
s = "GCGAAACAAAAAAGTTTTAACTTCCGAACCGTGCTCCTTATTCTGTCCGATGGAGTTTTGCTGGTAGGTGACAGATGTGTACTTTGCTCAAACCCCATTACGGATAACGTTCGTCACCGTGGAAATTCAGGTCAATCCGTATGGCCACAAAGGGTGTCTTGGGGGTCGTTACTGCACTTCCCGACAGTATTTAAGTAGTCGGAGTAGAAAGGAGGTAGGTGATATAATATACGATCTTGACGGTAGCCTACGTAACCCATCCGGATAATTAATCTTGACAATGGACGAGAGATAGCAGGCTTCAATACGGATTATTCCACTCTCTTCTCGAAGGCAGAAACCGCGGTGTATTCTAATCTAGCGATTATGCTGTAAAGATCGGTCTATCTCTATCCATGCAACAGTTTTAGGTTTTCCTTGCTTATCCATGGGACGGCTGCTCGTGTTAGTTAGAAGTATGATGATCCTTAACAACAGGTTGTCTCTCGTAAAGTGGCGAGGCCAGGTAACAGGGCGCGTCCTCGGCTCGCCGAGGGATTAAAGATACATCATCTTCCAACTTGGCAACCGGCAAATCCTTTCGGGAGGGGATCGCGGAGAGGGAGCAGTGACCGGCCTTCGCAAGAACACGGAGCCAAACCACCCCATAGACTAAAAGGAAAAAACAGCATCTCGGGGACTTGTCAAAGCTGGCCTTTAGTATCCGATGGATCATGTTAATGCCATCTCTAACAATGCCAGGGCGGTGGGATCCTCTGAATTTGCAGTAATACACTCAAACCTCTGACGCTTTCCCATTGGCAATAGCAGCAACTTCGAAGTAACGATTGGCTTCTAGCCAACAGTCTACTACTGAGAACGCGTCAT"
length_s = len(s)


def base_counter(input):
    bases = set(input)
    bases = list(bases)
    bases = sorted(bases)
    print(bases)

    test_bases = ['A', 'C', 'G', 'T']

    counts = []

    if bases == test_bases:
        for base in test_bases:
            base_count = s.count(base)
            #print(base, base_count)
            counts.append(base_count)
        return print(' '.join(str(i) for i in counts))

    else:
        print("Check the input.")


base_counter(s)


