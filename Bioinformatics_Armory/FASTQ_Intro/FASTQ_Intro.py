from Bio import SeqIO

x = SeqIO.parse("input.fastq", "fastq")
# print(next(x))

SeqIO.convert("input.fastq", "fastq", "output.fasta", "fasta")