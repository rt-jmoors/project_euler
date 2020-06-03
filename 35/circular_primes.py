
def find_primes(limit, starting_prime_list=[2]):
    """Returns a list of all prime numbers less than the limit given"""

    prime_list = starting_prime_list
    # prime_list = [2]
    number = prime_list[-1] + 1
    prime = True

    while number < limit:
        for prime in prime_list:
            if number % prime == 0:  # not prime
                prime = False
                break

        if prime:
            print('prime # ', len(prime_list), 'prime: ', number)
            prime_list.append(number)

        prime = True
        number += 1

    return prime_list


def rotate_digits(number):
    """Takes a number and returns a list of all rotations of the digits"""

    rotated_digits = [number]
    number = str(number)

    if len(number) == 1:
        # must be a single digit number
        return rotated_digits
    i = 1
    while i < len(number):
        number = number[1:] + number[0]
        rotated_digits.append(int(number))
        i += 1

    return extract_unique_list(rotated_digits)


def is_circular_prime(rotated, primes):
    """Returns True if all circular rotated digits appear in prime_list"""
    return all([prime in primes for prime in rotated])


def extract_unique_list(input_list):
    """Returns a list of unique values"""

    unique_list = []
    for i in range(0, len(input_list)):
        if input_list[i] not in input_list[0:i]:
            unique_list.append(input_list[i])
        else:
            continue

    return unique_list


limit = 2000
prime_list = find_primes(limit)
circular_prime_list = []
index = 0

# print(prime_list)

while len(prime_list) > 0:
    current_prime = prime_list[0]
    print('current prime:', current_prime)
    if is_circular_prime(rotate_digits(current_prime), prime_list):
        print('add to circular primes: ', rotate_digits(current_prime))
        circular_prime_list.extend(rotate_digits(current_prime))
    print(rotate_digits(current_prime))
    for x in rotate_digits(current_prime):
        if x in prime_list:
            print('removing: ', x)
            prime_list.remove(x)


# for elem in circular_prime_list:
#     print(circular_prime_list.index(elem)+1, elem)

print(len(circular_prime_list))

