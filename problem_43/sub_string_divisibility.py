

def is_divisible(num, divisor):
    if num % divisor == 0:
        return True
    return False


import itertools

lst = [*range(0, 10)]

divisors = [2, 3, 5, 7, 11, 13, 17]
pandigital_numbers = []

lst_permutations = []
for number in set(itertools.permutations(lst)):
    output_number = ''
    for digit in number:
        output_number += str(digit)
    lst_permutations.append(output_number)
print(len(lst_permutations))


counter = 0
for number_as_string in lst_permutations:
    print(counter, ': ', number_as_string)
    for i in range(0, len(divisors)):
        if not is_divisible(int(number_as_string[i+1:i+4]), divisors[i]):
            break
        pandigital_numbers.append(int(number_as_string))
        print('appending: ', number_as_string)
    counter += 1


sum_pan = 0
for elem in pandigital_numbers:
    print(elem)
    sum_pan += elem
print('sum of pandigitial numbers = ', sum_pan)


