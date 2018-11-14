from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

mrna = Seq(input("RNA to translate?"), IUPAC.unambiguous_rna)

print(mrna.translate(stop_symbol=""))