from Bio import ExPASy
from Bio import SwissProt, UniProt


query = "Q5SLP9"
handle = ExPASy.get_sprot_raw(query) #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins


for i in record.cross_references:
    if "GO" in i:
        if "P:" in i[2]:  # codes for GO TERM type = P, F, C
            print(i[2][2:])





