# a = int(input("A= "))
# b = int(input("B= "))

# c_squared  = a*a + b*b

# print(c_squared)

# ----

# string = input("String?")
#
# one = int(input("Slice 1: "))
# two = 1 + int(input("Slice 2: "))
# three = int(input("Slice 3: "))
# four = 1 + int(input("Slice 4: "))
#
# print(string[one:two], string[three:four])

# ----

# a = int(input("A= "))
# b = int(input("B= "))
#
# total = 0
#
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         pass
#     else:
#         total += i
#
# print(total)

# ----

# file = open("input.txt", "r")
# new_file = open("output.txt", "w")
# out_file = open("output.txt", "a")
#
# line_number = 1
#
# for line in file.readlines():
#     if line_number % 2 == 0:
#         out_file.write(line)
#     else:
#         pass
#
#     line_number += 1
#
# out_file.close()
# file.close()

# ----

string = input("String?")
# string = "We tried list and we tried dicts also we tried Zen"

string_list = string.split()
print(string_list)

list_dict = {}

for i in string_list:
    if i in list_dict.keys():
        list_dict[i] += 1
    else:
        list_dict[i] = 1

print(list_dict)

for i in list_dict:
    print(i, list_dict[i])




