# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

primes = [2, 3, 5, 7, 11, 13]
number = 14
prime = True

limit = 2000000

while primes[-1] < limit:
    for x in primes:
        if number % x == 0:  # not prime
            prime = False
            break

    if prime:
        # print(len(primes), number)
        if number > limit:
            break
        else:
            primes.append(number)

    prime = True
    number += 1

print('sum of primes below {}: '.format(limit), sum(primes))
