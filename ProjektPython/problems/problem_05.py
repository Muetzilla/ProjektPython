# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 20
while True:
    divisible = True
    for j in range(2, 21):
        if number % j != 0:
            divisible = False
            break

    if divisible:
        print(number)
        break

    number += 1