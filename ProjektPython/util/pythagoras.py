from math import sqrt


def calc_pyhtagoras(a, b):
    return sqrt(a**2 + b**2)

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2