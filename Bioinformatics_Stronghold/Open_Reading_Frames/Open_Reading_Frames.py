#! Documents/Rosalind/venv/bin/python

from Bio import SeqIO, Seq
from Bio.Alphabet import RNAAlphabet, DNAAlphabet
import sys
import regex as re

input_sequences = []

# for seqs in SeqIO.parse(f"{sys.argv[1]}", "fasta"):
for seqs in SeqIO.parse("input.fasta", "fasta"):
    input_sequences.append(seqs.seq)
    input_sequences.append(Seq.reverse_complement(seqs.seq))

print(input_sequences)
result_seqs = []

# Finds all ORFs with a start and stop codon in the seq range.

for seqs in input_sequences:

    window = 0

    for i in range(0, len(seqs)):
        # print(seqs[window:window+3])

        # Finds start codon in sequence
        if seqs[window:window+3] == "ATG":
            temp_result = [window]  # Stores start codon index in list.
            print("Start found:", seqs[window:window+3])

            # Finds first stop codon after start codon.
            temp_window = window
            for x in range(window, len(seqs)):
                if seqs[temp_window:temp_window+3] in ["TAG", "TAA", "TGA"]:
                    print("Stop found:", seqs[temp_window:temp_window+3])
                    temp_result.append(temp_window+3)  # Stores stop codon index in list with start codon.
                    break
                temp_window += 3  # Iterates by 3, codon size.

            # print(temp_result)
            # print(seqs[temp_result[0]: temp_result[1]])
            # result_seqs.append(seqs[temp_result[0]: temp_result[1]])

            # Adds protein to list from stored index locations, only if a stop codon is present at the end e.g.
            # a stop codon was found before the end of the sequence.
            try:
                dna = seqs[temp_result[0]: temp_result[1]]
                rna = Seq.transcribe(dna)
                protein = Seq.translate(rna, stop_symbol="")
                print(protein)
                if protein not in result_seqs:  # Stops the addition of duplicate peptides
                    result_seqs.append(protein)

            except IndexError:
                pass

        window += 1

print(result_seqs)

# Writes sequences to file.

file = open("result_peptides.txt", "w")
file.close()

for seqs in result_seqs:
    with open("result_peptides.txt", 'a') as outfile:
        print(seqs)
        outfile.write(str(seqs + "\n"))



# create array of all seqs, sort alphabetically, bin non ATG seqs ??