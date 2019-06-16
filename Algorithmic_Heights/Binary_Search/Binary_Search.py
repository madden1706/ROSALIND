#! /home/ross/anaconda3/envs/Rosalind/bin/python

import sys


# file = sys.argv[1]

file = "input.txt"

# Reading in the data from file.

with open(file, "r") as f:
    data = [line.strip() for line in f.readlines()]
    # print(data)

# Splitting the lines of the file into sensible variables.

int1 = int(data[0])
int2 = int(data[1])

array1 = data[3].split()
array2 = data[2].split()

print(f"Array to test; {array1}")
print(f"Binary Search Array: {array2}")


# Take array size. Get half.#


def recursive_search(start_pos):

    print('### Start search ###')

    array_size = start_pos

    position = start_pos//2
    print(f'Start: {position}')
    for i in array1:
        test = array2[position]
        print(f'Test: {test}, Array value: {i}')
        if test == i:
            print('match')
        else:
            print('no match')
            if test < i:
                print('Test value is smaller')
                position = array_size - (array_size - position)//2
                print(f'New pos: {position}')

            elif test > i:
                print('Test value is larger')
                position = position//2

                print(f'New pos: {position}')
        print('-----')


        #

recursive_search(int1)



# def binary_search(search_array, search_size, test_array, test_size):
#     # search_array are ints to search in the test_array.
#
#     results = []
#     pass
#
#
#
#
# binary_search(array2, int2, array1, int1)

# Check the value.
# If match get the result.
# If not take next half - recurse with input index value.
# Else return -1.
# Print results array

