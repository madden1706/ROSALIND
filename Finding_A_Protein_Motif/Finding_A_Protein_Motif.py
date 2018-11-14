from urllib import request
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.Seq import Seq
import regex as re


def get_input(file):
    """Reads requests from file. Returns a list of requests."""

    with open(file, "r") as input:
        read = input.readlines()

    data = [x.strip() for x in read]

    return data


def uniprot_api_access(requests):
    """Access UniProt API and return FASTA data."""

    output_file = open("finding_a_protein_motif.fasta", "w")

    for protein in requests:

        url = f"https://www.uniprot.org/uniprot/{protein}.fasta"
        print(url)

        with request.urlopen(url) as f:
            data = f.read().decode("utf-8")

            with open("finding_a_protein_motif.fasta", "a") as out:
                out.write(data)


def motif_search(motif, proteins, ids):

    records = list(SeqIO.parse(proteins, "fasta"))
    output_file = open("finding_a_protein_motif_output.txt", "w")

    for i in range(0, len(records)):
        # print(records[i].id)
        # id = re.search("[|].*[|]", records[i].id)
        # id = id.group().strip("|")
        # print(id)

        search = re.finditer(motif, str(records[i].seq), overlapped=True)

        start_pos = ""

        for j in search:
            pos = (j.start()+1)
            start_pos = start_pos +f"{pos} "
        print(start_pos)
        id = ids[i]

        data = [id, start_pos]
        print(data)
        if data[1] == "":
            pass
        else:
            with open("finding_a_protein_motif_output.txt", "a") as out:
                out.write(id)
                out.write("\n")
                out.write(start_pos)
                out.write("\n")


in_data = get_input("finding_a_protein_motif.txt")
print(in_data)
uniprot_api_access(in_data)

search_motif = "N[^P][ST][^P]"

motif_search(search_motif,"finding_a_protein_motif.fasta", in_data)
