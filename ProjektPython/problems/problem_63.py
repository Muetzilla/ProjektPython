# Problem 63
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

number_of_n_digit_powers = 0

for exponent in range(1, 100):
    for base in range(1, 10):
        if len(str(base ** exponent)) == exponent:
            number_of_n_digit_powers += 1
        elif len(str(base ** exponent)) > exponent:
            break


print(number_of_n_digit_powers)
