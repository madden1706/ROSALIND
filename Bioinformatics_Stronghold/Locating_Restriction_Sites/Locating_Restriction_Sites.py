from Bio import Seq, SeqIO
import timeit

x = [seqs for seqs in SeqIO.parse("input.fasta", "fasta")]
y = x[0].reverse_complement().seq
y = y[::-1] + "!"
x = x[0].seq + "£"  # These are unique values to stop the ends of strings evaluating as identical when slices reach the end.

print(x, y)

open("output.txt", "w")

for i in range(0, len(x)):
    for j in range(4, 13):
            if len(x[i: i+j]) > 3:
                seqF = x[i: i + j]
                seqR = y[i: i + j]
                seqR = seqR[::-1]
                # print(seqF, "=", seqR)

                if seqF == seqR:
                    data = str(i+1)
                    data += " "
                    data += str(len(seqF))
                    print(data)
                    with open("output.txt", "a") as outfile:
                        outfile.write(data)
                        outfile.write("\n")

