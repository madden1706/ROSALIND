import subprocess
from Bio import SeqIO
import pandas as pd

# http://hannonlab.cshl.edu/fastx_toolkit/commandline.html

x = []

with open("input.fastq", "r") as file:
    x = file.readlines()
    # print(x)

threshold = int(x[0])
print("Threshold:", threshold)
x = x[1:]

with open("input2.fastq", "w") as file:
    file.writelines(x)

reads = SeqIO.parse("input2.fastq", "fastq")

reads_below_threshold = 0

reads_df = pd.DataFrame()
x = 0
for i in reads:
    reads_df[f"{x}"] = i.letter_annotations["phred_quality"]
    # {i.id}_

    x += 1

reads_df["mean"] = reads_df.mean(axis=1)
reads_df["per_base_quality"] = reads_df.mean(axis=1) < threshold

print(reads_df)


print("Number of positions where mean base quality falls below given threshold:", reads_df["per_base_quality"].value_counts()[1])
