#!/usr/bin/env python3 

from collatz_conjecture import collatz

print("Please supply the start and end values. Ex: 5, 12")
values_str = input(" : ")

values = values_str.split(', ')
values = int(values[0]), int(values[1])

for n in range(values[0], values[1]+1):
    print(collatz(n))


