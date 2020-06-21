def is_pandigital(num):
    """Determines if a number is pandigital or not

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
    5 pandigital.
    """
    digits = set(str(num))
    for digit in digits:
        if int(digit) > len(str(num)):
            return False
        elif str(num).count(digit) > 1:
            return False
    return True


def is_product(mult1, mult2, product):
    if mult1 * mult2 == product:
        return True
    return False

import datetime
import itertools
begin_time = datetime.datetime.now()

strng = '123456789'

perms = []
for i in itertools.permutations(list(strng)):
    perms.append(''.join(i))

products = []
for x in perms:
    # 2 is subtracted because to have 3 complete terms, we need at least 2 digits for the multiplicand/multiplier
    for i in range(0, len(x) - 2):
        # Select product from the end of the numbers
        product = int(x[-1 - i:])
        for j in range(0, len(x) - 2 - i):
            # Multiplicand is at least 1 number, starting from the beginning of the numbers
            multiplicand = int(x[0:j + 1])
            # The multiplier is the numbers remaining between the multiplicand and the product
            multiplier = int(x[j + 1:-1 - i])
            if is_product(multiplicand, multiplier, product):
                print(multiplicand, '*', multiplier, '=', product)
                if product not in products:
                    products.append(product)

print('Sum of pandigital products =', sum(products))

print(datetime.datetime.now() - begin_time)