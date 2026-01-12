# Problem 6
# What is the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum?

sum_of_squares = 0
number_range = 100
for i in range(1, number_range + 1):
    sum_of_squares += i ** 2

print((number_range * (number_range + 1) // 2 )** 2 - sum_of_squares)