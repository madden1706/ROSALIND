import subprocess
from Bio import SeqIO, Seq

input_file = "input.fasta"

# getorf -sequence input.fasta -outseq output.fasta -find 1
# Finds all ORFs starting with M.
subprocess.run([f"getorf -sequence {input_file} -outseq output.fasta -find 1"], shell=True)
# http://emboss.sourceforge.net/apps/cvs/emboss/apps/getorf.html

length = 0
result_seq = ""

seqs = SeqIO.parse("output.fasta", "fasta")
for x in seqs:  # Returns longest ORF starting with M.
    if len(x.seq) > length:
        length = len(x.seq)
        result_seq = x

print(result_seq.seq)








