from Bio.Seq import Seq
from Bio import motifs

from Bio import SeqIO


instances = []

for seq_record in SeqIO.parse("Consensus_and_Profile.txt", "fasta"):
    instances.append(seq_record.seq)

m = motifs.create(instances)

print(m.consensus)  # fine.
#print(m.counts)  # needs formatting correctly.

# refromats for entry - correct.
bases = ["A", "C", "G", "T"]

for base in bases:
    print (base + ":", end=" ")
    for i in m.counts[base]:
        print(i, end=" ")
    print("")





