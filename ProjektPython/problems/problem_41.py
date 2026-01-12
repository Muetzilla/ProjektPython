# Problem 41
# We shall say that an -digit number is pandigital if it makes use of all the digits  to  exactly once. For example,  is a -digit pandigital and is also prime.
#
# What is the largest -digit pandigital prime that exists?
from util.prime import is_prime
from itertools import permutations

for length in range(7, 0, -1):
    digits = ''.join(str(i) for i in range(length, 0, -1))
    for perm in permutations(digits):
        num = int(''.join(perm))
        if is_prime(num):
            print(num)
            break
    else:
        continue
    break