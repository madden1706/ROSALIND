from Bio import Entrez
from Bio import SeqIO

Entrez.email = "madden1706@gmail.com"

search = ["NM_001159758", "NM_214399", "NM_001168970", "JQ011270", "JX393321",
          "JX491654", "NM_001135551", "NM_001194889", "NM_001003102"]

handle = Entrez.efetch(db="nucleotide", id=search, rettype="fasta")  # id=f'{search}')
records = list(SeqIO.parse(handle, "fasta"))

shortest = (0, 1000000000, "")

for i in range(0, len(records)):
    # print(len(records[i].seq), records[i].id)
    if len(records[i].seq) < shortest[1]:
        shortest = (i, len(records[i].seq), records[i].id)
        # print("Updated: ", shortest)
    else:
        pass

print("Result: ", shortest)
result_id = shortest[2]

# https://www.ncbi.nlm.nih.gov/books/NBK25499/table/chapter4.T._valid_values_of__retmode_and/?report=objectonly
handle2 = Entrez.efetch(db="nucleotide", id=f"{result_id}", rettype="fasta", retmode="text")
print(handle2.read())