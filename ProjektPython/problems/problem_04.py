# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
from util.palindrome import is_palindrome_number

largest_palindrome = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if is_palindrome_number(product) and product > largest_palindrome:
            largest_palindrome = product
print(largest_palindrome)