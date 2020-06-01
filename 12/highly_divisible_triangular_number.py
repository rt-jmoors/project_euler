
def find_factors(x):

    largest_divisor = x
    i = 1
    factors = []
    if x == 1:
        return [1]
    while i < largest_divisor:
        if x % i == 0:
            if i == x//i:
                factors.append(i)
            else:
                factors.extend((i, x//i))
            largest_divisor = x // i

        i += 1

    factors.sort()
    return factors

limit = 500
number = 2
triangle_number = 1

while True:
    print('Triangle number = ', triangle_number, end=' ')
    factors = find_factors(triangle_number)
    print('Factors: {}'.format(len(factors)))
    if len(factors) > limit:
        print('Solution found ^^')
        break

    triangle_number += number
    number += 1

print('Number with more than {} divisors: '.format(limit), triangle_number)
