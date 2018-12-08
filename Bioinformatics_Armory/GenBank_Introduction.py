from Bio import Entrez

Entrez.email = "madden1706@gmail.com"

date1 = "2004/08/15"
date2 = "2006/04/15"
genus = "Chenopodium"

handle = Entrez.esearch(db="nucleotide", term=f'"{genus}"[ORGANISM] AND ("{date1}"[PDAT] : "{date2}"[PDAT])')

# ("2003/06/17"[MDAT] : "2003/06/19"[MDAT]) = date search format.
record = Entrez.read(handle)

print("Count:", record["Count"])
for i in record:
    print(i, ":", record[i])

