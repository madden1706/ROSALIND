from Bio import Seq, SeqIO

result = []
counter = 0

for x in SeqIO.parse("input.fasta", "fasta"):
    print(x.seq)
    print(x.reverse_complement())

    if x.seq == x.reverse_complement().seq:
        result.append(x)
        counter += 1

SeqIO.write(result, "output.fasta", format="fasta")
print(counter)




