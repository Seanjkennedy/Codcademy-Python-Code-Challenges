# 9 Rearrange the number

"""To complete this challenge, write a function that accepts a number as a parameter. The function should return a number 
that’s the difference between the largest and smallest numbers that the digits can form in the number.

For example, if the parameter is "213", the function should return "198", which is the result of 123 subtracted from 321."""


def large_minus_small(number):

    smallest = sorted(str(number))
    largest = int("".join(smallest[::-1]))
    smallest = int("".join(smallest))

    return largest - smallest


print(large_minus_small(213))
print(large_minus_small(132465))