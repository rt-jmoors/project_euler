# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import sys

triplets = []
value_found = False


def is_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


for c in range(1000, 1, -1):
    for b in range(c-1, 1, -1):
        for a in range(b - 1, 1, -1):
            if is_triplet(a, b, c) and sum((a, b, c)) == 1000:
                print('triplet = ', a, b, c)
                print('product abc =', a * b * c)
                sys.exit(0)
            else:
                continue

