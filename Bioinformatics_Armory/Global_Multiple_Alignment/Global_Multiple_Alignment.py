from Bio import SeqIO, Seq
from Bio.Align.Applications import ClustalwCommandline
import subprocess
from Bio import Phylo, AlignIO

seq = SeqIO.parse("input.fasta", "fasta")
cline = ClustalwCommandline("clustalw", infile="input.fasta",)

subprocess.run(str(cline), shell=True)

tree = Phylo.read("input.dnd", "newick",)

print(tree, "\n")
Phylo.draw_ascii(tree)

# Search branch length or view tree for most distantly related, NB/ tree types.


