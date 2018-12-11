from Bio import SeqIO
from Bio.Seq import Seq
from Bio import motifs
from Bio.Alphabet import IUPAC
import xml.etree.ElementTree as ET
import subprocess

# Used MEME (v5.0.3) locally find motif.
# Script takes fasta file of from the MEME output as "meme_fasta_output.fasta".
# Returns a regular expression of the motif.

subprocess.run(["meme input.fasta"], shell=True, check=True)

tree = ET.parse('meme_out/meme.xml')
root = tree.getroot()

print("Regular expression", root[2][0][2].text)


# ----- Redundant with xml parsing.

seqs = SeqIO.parse("meme_fasta_output.fasta", "fasta", alphabet=IUPAC.protein)

sequences = [x.seq for x in seqs]  # Seq(str(x.seq))
# print(sequences)

m = motifs.create(sequences, alphabet=IUPAC.protein)  # Needs to have the correct character alphabet specified.
# print(m)


def residue_list(input_motif):
    """Takes argument of a motif from BioPython motifs.create"""
    residues = []
    for i in range(0, input_motif.length):
        temp_list = []
        for x in input_motif.instances:
            if x[i] in temp_list:
                pass
            else:
                temp_list.append(x[i])

        residues.append(temp_list)

    return residues


def regex_generator(input_list):

    regex = ""

    for x in range(0, len(input_list)):
        # print(input_list[x])
        if len(input_list[x]) == 1:
            regex += input_list[x][0]
        else:
            # pass
            res = "".join(input_list[x])
            regex += f"[{res}]"

    return print("Regex:", regex)


# ----- Redundant with xml parsing - END.
# list_to_regex_expression = residue_list(m)
# regex_generator(list_to_regex_expression)
# print("Consensus:", m.consensus)