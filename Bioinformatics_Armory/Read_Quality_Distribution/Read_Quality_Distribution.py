from Bio import SeqIO

x = []

with open("input.fastq", "r") as file:
    x = file.readlines()
    print(x)

threshold = int(x[0])
print(threshold)
x = x[1:]

with open("input2.fastq", "w") as file:
    file.writelines(x)


good_reads = (rec for rec in SeqIO.parse("input2.fastq", "fastq")  # If average quality below threshold.
              if sum(rec.letter_annotations["phred_quality"])/len(rec.seq) < threshold)

count = SeqIO.write(good_reads, "good_quality.fastq", "fastq")

print("Saved %i reads above average threshold quality." % count)


