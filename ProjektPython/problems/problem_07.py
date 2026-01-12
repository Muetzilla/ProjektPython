# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from util.prime import is_prime

prime_count = 1
number = 1
while prime_count < 10001:
    number += 2
    if is_prime(number):
        prime_count += 1
print(number)