from Bio.Seq import Seq
from Bio.Alphabet import ProteinAlphabet, RNAAlphabet
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import numpy as np

# dict of number of codons.
codon_dict = {"F": 2, "L": 6, "S": 6, "Y": 2, "*": 3, "C": 2, "W": 1, "P": 4, "H": 2, "Q": 2, "R": 6, "I": 3, "M": 1,
              "T": 4, "N": 2, "K": 2, "V": 4, "A": 4, "D": 2, "E": 2,  "G": 4}

# Protein string to assess.
protein = "MTHCQFWPTREEYWKTPYGFKDPQMILGTNYYMAAALDHEPHFAMVTVWFDCVFPWGAVEHMCNCQGENDVWDKQAHPQLRMKGSFPWQFSQRREMPIPFQQSVYHMIQLCWDTSGRMSKQPQNTSANKYTMLQMKHFNNCCVTCGREYRDEVDLLNMTLGGDYYDYAWTQNMDLIARMYRTGNHTKERAILGMCWPGGMRHHIALFFLKTVGYALMHPNCGMRFYNWICFEHMMGIRGRFWWLCFNISHRMPDSPHDIDLDWVIHARYCCQKEMLEILEISHCHSGWIYDPGKLWFDVNQSSWEEERVQPVNEYNQQVAWNVPNLWQSEVENNVMTVICDIDCVTAEQNVFRVSTLYNTAPQAFRVHTHFFPMCIFKHWASTMFFVWYIFLFETRWGHLWWKHLLMWWRLYWTWNCQYLPLWSEVAAMNSKDMYSTPPKSLPIHDWHNQKTAHSGGVKDWCIPCIQCPHNGCTHDDGSLLHFTPHMFSMWNRDIWADLNCQMMETWNFTMKLRYHERITWSDPDNRNNGAQFRSFQLNWIFHAPKTGGKGWFKEHYWFQMDMNWHNWSDTLYFNCGIVSVYPMSEGRDRIGQLPFCRKAWSIRQWFGFMSYIAEARACITWDHAVFTPWDMTDNDLSANNNKSSGQAHILDTWDWVEQDLEDEAAGPPPYNYSNCAIEDYMFDQAWPFLYYYFWTVICMHGVHEQNMWTDFFLMQGQIYVQSANQCEGIWQGVYPDGEPTHLKKEWDLMAHDTGNYYKVHDWWPYHECIHCWQDEWTTYCFPRLSIMYKFLEGGTCKLDSKRWELNDEEVFGHPFEQTISIGRLQYHSPLDKHEPMKSHIVVWDASGYRGFSTCLTNERMTEWQPTWKDKCLHKTNHDCAEGNVRKFEARQCKLYIMSPQTVFMFGMFAGNWTCWHDEDYGTWLSTPVGLDGHIISMQPCEVNMDYDSSDTEPNTFNAAFNACSRIHMRQKVIQGLREYFHAAEFKAYSVKDGGNM"
# Add stop codon.
protein = protein + "*"

# Making array of residues.
y = [i for i in protein]
# print(y)
# Covert residues to number of possible codons.
y2 = np.array([codon_dict[i] for i in y])
print("Array of codon counts:", y2)

# https://stackoverflow.com/questions/2177781/how-to-calculate-modulus-of-large-numbers

modulo = 1000000
millions = 1
prod = 1

for i in range(0, len(y2)):

    prod = prod * y2[i]
    # print("Product", prod)
    if prod > modulo:
        temp = round(prod//modulo)
        print(temp)
        # millions = millions * temp
        prod = prod % modulo

    else:
        pass

# print("Millions", millions)  # Wrong, no idea why yet...
print(prod, "mod", modulo)





