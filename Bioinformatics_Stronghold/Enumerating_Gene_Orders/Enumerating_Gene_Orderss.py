from itertools import permutations
import math
import os



perm_value = 6

intergers = [i for i in range(1, perm_value + 1)]

x = permutations(intergers)

file = open("output.txt", "w")

file.close()

with open("output.txt", "w") as outfile:
    total = math.factorial(perm_value)
    outfile.write(str(total) + "\n")

for i in x:
    with open("output.txt", "a") as outfile:
        for x in range(0, perm_value):
            outfile.write(str(i[x]) + " ")
        outfile.write("\n")
