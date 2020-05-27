# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

limit = 10000
target = 600851475143
factor_list = []
prime_list = [2]
num_is_prime = True

for num in range(3, limit):
    num_is_prime = True
    for prime in prime_list:
        if num % prime == 0:
            # not a prime number, as a prime number is a factor
            num_is_prime = False
            break
    # finished the for loop, 'num' must be prime
    if num_is_prime:
        prime_list.append(num)
        if target % num == 0:
            factor_list.append(num)
        # break
product_factors = 1
for elem in factor_list:
    product_factors *= elem
    print('primes which are a factor of target: ', elem)

print('product of factors = ', product_factors)


