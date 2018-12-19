import subprocess
from Bio import SeqIO


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

# http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf

subprocess.run("java -jar /home/ross/bin/Trimmomatic-0.38/trimmomatic-0.38.jar "
               f"SE -phred33 input2.fastq output.fastq LEADING:{threshold} TRAILING:{threshold}", shell=True)


