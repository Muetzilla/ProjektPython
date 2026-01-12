# Problem 10
# The sum of the primes below two million.

from util.prime import is_prime

limit = 2_000_000
prime_sum = 0
for i in range(2, limit+ 1):
    if is_prime(i):
        prime_sum += i

print(prime_sum)