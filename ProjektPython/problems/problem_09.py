# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5²
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from util.pythagoras import is_pythagorean_triplet

target_sum = 1000
for a in range(1, target_sum):
    for b in range(a + 1, target_sum - a):
        c = target_sum - a - b
        if is_pythagorean_triplet(a, b, c):
            print(a * b * c)
            break