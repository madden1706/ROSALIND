from Bio.Seq import Seq

dna = Seq("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

print(dna.count("A"), dna.count("C"), dna.count("G"), dna.count("T"))

