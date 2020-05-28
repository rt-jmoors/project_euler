# 2520 is the target number that can be divided by each of the numbers from 1 to 10
# without any remainder.

# What is the target positive number that is evenly divisible by all of the numbers from 1 to 20?

# Notes:
# The number will have to be a multiple of 380, as this is the smallest number in which both 20 & 19
# are divisible (as these are the two largest numbers we are inspecting).
# Therefore, starting with 380, go through multiples of 380, checking from 18 to 11 if any of these
# numbers evenly divide (numbers 10 through 1 don't need to be checked, as if numbers 18 to 11 are
# factors, then numbers 10 through 1 are factors as well given they are factors of 18 -> 11).

factors = [*range(18, 10, -1)]

target = 380
found = False
remainder = True
while not found:

    for number in factors:
        print(target, number)
        if target % number != 0:
            remainder = True
            target += 380
            break

    if not remainder:
        found = True
        print('target found = ', target)
        break

    remainder = False


