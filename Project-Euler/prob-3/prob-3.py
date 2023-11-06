'''
# Largest Prime Factor

The prime factors of 13195 are 5, 7, 13, and 29. 
What is the largest prime factor of the number 600851475143?
'''

from math import sqrt

primes = []
test_num = 600851475143

def get_factors(factor_number):
    factors = []
    limit = sqrt(factor_number)
    i = 1

    while i < limit:
        if factor_number % i == 0:
            print("Factor found: " + str(i))
            factors.append(i)
            factors.append(int(factor_number / i))
        
        i += 1

    factors.sort()
    return factors

print(get_factors(test_num))