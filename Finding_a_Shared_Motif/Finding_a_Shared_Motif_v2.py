from Bio import Seq, SeqIO
from itertools import permutations
import sys
import subprocess

input_fasta = sys.argv[1]
# input_fasta = "input.fasta"

# --- CREATE SENTINEL VALUES ---
sentinel_values = [chr(x) for x in range(33, 65)]   # use ! (33) to @ (64) for sentinel values.
sentinel_number = 2  # for 2 permutations = 992 values. 3  = 29822
sentinel_values_permutations = permutations(sentinel_values, sentinel_number)
# (values ^ permutations)  - (values ^ (permutations-1))

sentinel_values_permutations_list = []

limit = 0
for i in sentinel_values_permutations:  # TODO should pre-make and store this list.
    if limit == 992:
        break
    else:
        sentinel_values_permutations_list.append("".join(i))
    limit += 1

# --- CREATE SUBSTRINGS  ---
open("concat_substring.txt", "w")

# Parse file for sequences and add to file with sentinel values.
# Only add string to distal sentinel value i.e. not concatenated.

index = 0
sentinel_values_used = []  # Used in sliding windows analysis.
for seq in SeqIO.parse(input_fasta, "fasta"):

    with open("concat_substring.txt", "a") as output:
        string_plus_sentinels = str(seq.seq) + sentinel_values_permutations_list[index]
        sentinel_values_used.append(sentinel_values_permutations_list[index])

        for x in range(0, len(seq.seq)):
            # print(str(seq.seq)[x:] + sentinel_values_permutations_list[index])
            output.write(("{}\n".format(str(seq.seq)[x:] + sentinel_values_permutations_list[index])))

        index += 1

# --- SORT SUBSTRINGS ---
subprocess.run(["sort concat_substring.txt -o concat_substring.txt"], shell=True, check=True)

# --- CREATE PREFIX, LCS LENGTH & LCS STRING ARRAYS ---
line_one = ""
line_two = "X"
prefix_array = []
suffix_array = []
string_array = []

with open("concat_substring.txt", "r") as substring_array:

    for line in substring_array.readlines():
        line_one = line
        suffix_array.append(line_one[-3:-1])
        prefix_length = 0

        for x in range(0, len(line_one)-1):  # evaluates the strings for matches
            if (line_one[x] not in sentinel_values) and (line_two[x] not in sentinel_values) and line_one[x] == line_two[x]:
                prefix_length += 1
                # print(line_one[x], ":", line_two[x])
            else:
                prefix_array.append(prefix_length)
                string_array.append(line_one[0:prefix_length])
                line_two = line_one
                break

# print(len(prefix_array), prefix_array)
# print(len(suffix_array), suffix_array)
# print(len(string_array), string_array)

# --- SLIDING WINDOW ANALYSIS ---

window = [0, 1]
result_array = []
lcp_value = 0


while window[1] < len(string_array) + 1:  # TODO does this get to the end correctly? With window[0] evaluation?
    if set(suffix_array[window[0]: window[1]]) ==set(sentinel_values_used):

        # print("match")
        # print("yes", set(suffix_array[window[0]: window[1]]))

        # dictates the prefix length ot return.
        prefix_to_return = prefix_array[window[0]:window[1]]
        prefix_to_return.pop(0)
        prefix_to_return = sorted(prefix_to_return)

        # print(prefix_to_return[0])
        # print(str(sorted_suffix_array[window[1]-1][0:prefix_to_return[0]]))

        if lcp_value < prefix_to_return[0]:
            result_array = [str(string_array[window[1] - 1][0:prefix_to_return[0]])]
            lcp_value = prefix_to_return[0]
        elif lcp_value == prefix_to_return[0]:
            result_array.append(str(string_array[window[1] - 1][0:prefix_to_return[0]]))
        else:
            pass
        # print(lcp_value)
        window[0] = window[0] + 1

    else:
        # print(window)
        # print("no", set(suffix_array[window[0]: window[1]]))
        window[1] = window[1] + 1

print("Longest commong substrings are:")
for i in result_array:
    print(i)


