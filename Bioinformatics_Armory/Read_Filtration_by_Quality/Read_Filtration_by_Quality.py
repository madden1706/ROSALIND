import subprocess
from Bio import SeqIO

# http://hannonlab.cshl.edu/fastx_toolkit/commandline.html

threshold_value = 20
percent_bases = 87

subprocess.run([f"fastq_quality_filter -i input.fastq -q {threshold_value} -p {percent_bases} -o output.fastq"], shell=True)

seq = SeqIO.parse("output.fastq", "fastq")
count = 0

for i in seq:
    count += 1

print("Above quality values:", count)


