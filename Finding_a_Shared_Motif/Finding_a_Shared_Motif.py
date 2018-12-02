from Bio import Seq, SeqIO, AlignIO
from Bio.SeqRecord import SeqRecord
from itertools import permutations, combinations
import re


# https://www.youtube.com/watch?v=Ic80xQFWevc


# Create array of sentinel values.

# use ! (33) to @ (64) for sentinel values.
sentinel_values = [chr(x) for x in range(33, 65)]  # 33, 65 for ascii "!" up to "A".
sentinel_values_permutations = permutations(sentinel_values, 2)  # for 2 permutations = 992 values. 3  = 29822
# (values ^ permutations)  - (values ^ (permutations-1))


# Concatenate together with sentinel values, unique "#, %, $"

concat_string = ""
index = 0
for seq in SeqIO.parse("input.fasta", "fasta"):
    concat_string += seq.seq + sentinel_values[index]
    index += 1
print(concat_string)


# Make suffix array -  going to need to handle the multiple sentinels.

start = 0
end = len(concat_string)
print(f"String length is {end}. \n")
suffix_array = [concat_string[x:end] for x in range(start, end)]
sorted_suffix_array = sorted(suffix_array)

while sorted_suffix_array[0][0] in sentinel_values:  # Remove strings starting with sentinel value.
    sorted_suffix_array.pop(0)

print("Suffix Array size:", len(sorted_suffix_array))

print("Array:")
for i in sorted_suffix_array:
    print(i)
print("End array.\n")


# Build Longest-Common Prefix array
# ------------------------------------------------------
# ~# AATTTAA ~@
#       TTAA ~# deal with by if value is > suffix limit stop. Then it will only match TTAA, not TTAA~
# sort suffixes - check that if multiple suffixes are included seqs are removed.
# ------------------------------------------------------

prefix_array =[]

a, b = sorted_suffix_array[0], sorted_suffix_array[1]

for i in range(0, len(sorted_suffix_array)-1): # evaluates the strings for matches

    prefix_length = 0
    for x in range(0, len(sorted_suffix_array)-1):
        if (a[x] and b[x] not in sentinel_values) and (a[x] == b[x]):
            prefix_length += 1
            x = +1
        else:
            prefix_array.append(prefix_length)
            break

    if i+1 == len(sorted_suffix_array)-1:
        break
    else:
        a, b = b, sorted_suffix_array[i+2]
        #print("a:", a, "b:", b)

prefix_array.insert(0, 0)
# print(prefix_array)

# Finds the first suffix of the string and returns to array.
sentinel_sorted_suffix_array = []

for i in sorted_suffix_array:
    search = re.search(r'[!"#$%&\'()*+,\-./0123456789]+', str(i)) # regex to get 1st sentinel value.
    x = search.start()
    y = search.end()

    try:
        sentinel_sorted_suffix_array.append(str(i[x:y]))
    except:
        sentinel_sorted_suffix_array.append(str(i[x]))

suffix_length_array = [(a, b, c) for a, b, c in zip(prefix_array, sentinel_sorted_suffix_array, sorted_suffix_array, )]

pos = 0
for i in suffix_length_array:
    print(pos, " ", i[0], " ", i[1], " ", i[2])
    pos += 1


# Sliding Window Analysis of LCP Array

# make window
window = [0, 1]
result_array = []
lcp_value = 0

sentinel_values_used = set(re.findall(r'[!"#$%&\'()*+,\-./0123456789]', str(concat_string)))

while window[1] < len(sorted_suffix_array): # TODO does this get to the end correctly? With window[0] evaluation?
    if set(sentinel_sorted_suffix_array[window[0]: window[1]]) == sentinel_values_used:

        # print("match")
        # print("yes", set(sentinel_sorted_suffix_array[window[0]: window[1]])

        # dictates the prefix length ot return.
        prefix_to_return = prefix_array[window[0]:window[1]]
        prefix_to_return.pop(0)
        prefix_to_return = sorted(prefix_to_return)

        # print(prefix_to_return[0])
        # print(str(sorted_suffix_array[window[1]-1][0:prefix_to_return[0]]))

        if lcp_value < prefix_to_return[0]:
            result_array = [str(sorted_suffix_array[window[1] - 1][0:prefix_to_return[0]])]
            lcp_value = prefix_to_return[0]
        elif lcp_value == prefix_to_return[0]:
            result_array.append(str(sorted_suffix_array[window[1]-1][0:prefix_to_return[0]]))
        else:
            pass
        # print(lcp_value)
        window[0] = window[0] + 1

    else:

        # print(window)
        # print("no", set(sentinel_sorted_suffix_array[window[0]: window[1]]))
        window[1] = window[1] + 1

print("Longest commong substrings are:")
for i in result_array:
    print(i)


# expand if do not have all prefixes

# if have all, store not 0 smallest LCP value and seq

# shrink window and repeat




# ----------------





