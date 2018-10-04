from Bio.Seq import Seq
from Bio import motifs


def motif_find(dna, motif_to_search):
    """Finds all instances of a motif in a string, returns str of start positions"""

    instances = [Seq(motif_to_search)]
    m = motifs.create(instances)

    listOfStartPostitions = ""

    for pos, seq in m.instances.search(dna):
        print("{0}, {1}".format(pos+1, seq))
        listOfStartPostitions +="{0} ".format(pos+1)

    return print(listOfStartPostitions)

file = "Finding_a_Motif_in_DNA.txt"
with open(file, "r") as f:
    dna = f.read()


motif_find(dna, "GCCGTACGC")