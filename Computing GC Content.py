from Bio.SeqUtils import GC
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO


def highest_gc_finder(self):
    """From a fasta file, returns the seq id and GC contect as % of highest GC seq."""

    samples = ()

    gc = 0.0
    id = ""

    for record in SeqIO.parse(self, "fasta"):
        samples = samples + (record.id, round(GC(record.seq, ), 6))

        if gc < round(GC(record.seq, ), 6):
            gc = round(GC(record.seq, ), 6)
            id = record.id
        else:
            pass

    print("{}\n{}".format(id, gc))


highest_gc_finder("test.fasta")