from Bio.Seq import translate, Seq, Alphabet, CodonTable


with open("input.txt", "r") as file:
    x = file.read().splitlines()
    # print(x)

dna = Seq(x[0], Alphabet.generic_dna)
protein = Seq(x[1]+"*", Alphabet.generic_protein)  # * = stop codon.

print(dna+"\n", protein)

translations = []

# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi

print(CodonTable.unambiguous_dna_by_id.keys())

for x in CodonTable.unambiguous_dna_by_id.keys():
    trans_dna = translate(dna, table=x, stop_symbol="*")
    translations.append((x, trans_dna))

CodonTable.unambiguous_dna_by_id.keys()


# x = translate(dna, table=2, to_stop=True)
print(translations)

for i in translations:
    if i[1] == protein:
        print("Table used:", i[0])

