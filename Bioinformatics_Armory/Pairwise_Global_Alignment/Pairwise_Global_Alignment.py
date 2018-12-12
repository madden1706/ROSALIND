# Installed EMBOSS locally.

from Bio import Entrez
from Bio import SeqIO
from Bio.Emboss.Applications import NeedleCommandline
import subprocess



Entrez.email = "madden1706@gmail.com"

search = ["JX205496.1", "JX469991.1"]  # take input from file.
# search = ["JQ290344.1", "JX317624.1"]

handle = Entrez.efetch(db="nucleotide", id=search, rettype="fasta")  # id=f'{search}')
records = list(SeqIO.parse(handle, "fasta"))
print(records)

files_created = []

for i in records:
    id = i.id
    with open(f"{id}.fasta", "w") as output_handle:
        SeqIO.write(i, output_handle, "fasta")
    files_created.append(f"{id}.fasta")

# pairwise alignment


output_file = "_".join(search)
output_file = output_file[1:]
output_file = output_file + ".txt"

pairwise = NeedleCommandline(asequence=f"{files_created[0]}", bsequence=f"{files_created[1]}", gapopen=10, gapextend=1,
                             endopen=10, endextend=1, endweight=True,
                             # emboss.sourceforge.net/apps/cvs/emboss/apps/needle.html
                             outfile=output_file)


subprocess.run([str(pairwise)], shell=True, check=True)

with open(output_file, "r") as f:
    for line in f.readlines():
        if "Score" in line:
            print(line)





