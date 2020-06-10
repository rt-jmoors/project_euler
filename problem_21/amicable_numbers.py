def proper_divisors(number):
    """Takes a number and returns a list of the proper divisors"""

    if number < 0:
        return

    elif number == 1:
        return [1]

    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    return divisors


def d(n):
    """Sum the proper divisors of number n"""
    return sum(proper_divisors(n))


limit = 10000

amicable_numbers = []
for a in range(1, limit):
    # print('i =', i)
    if a in amicable_numbers:
        continue
    b = d(a)
    if a != b and d(b) == a:
        print('amicable = ', (a, b))
        amicable_numbers.extend([a, b])

print('sum of amicable numbers = ', sum(amicable_numbers))
