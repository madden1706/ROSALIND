import subprocess
from Bio import SeqIO, Seq

input_file = "input.fasta"

# getorf -sequence input.fasta -outseq output.fasta -find 1
subprocess.run([f"getorf -sequence {input_file} -outseq output.fasta -find 1"], shell=True)

length = 0
result_seq = ""

seqs = SeqIO.parse("output.fasta", "fasta")
for x in seqs:
    if len(x.seq) > length:
        length = len(x.seq)
        result_seq = x

print(result_seq.seq)








