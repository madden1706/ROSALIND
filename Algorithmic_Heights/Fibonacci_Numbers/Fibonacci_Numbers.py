import timeit
import sys

number = int(input("What interger? "))


def fib1(input_int):

    if input_int == 0:
        output = 0
        return output

    elif input_int == 1:
        output = 1
        return output

    else:
        output = fib1(input_int - 1) + fib1(input_int - 2)
        return output


def fib2(input_int):

    if input_int == 0:
        return 0

    elif input_int == 1:
        return 1

    else:
        fib_numbers = [0, 1]
        for i in range(0, input_int):
            fib_numbers.append(fib_numbers[0 + i] + fib_numbers[1 + i])

        return fib_numbers[input_int]

out1 = fib1(number)
out2 = fib2(number)

# fib2 is faster than fib1 as the function only needs to loop once.

print(f"The {number}th value in Fibonacci number is {out1}")
print(f"The {number}th value in Fibonacci number is {out2}")