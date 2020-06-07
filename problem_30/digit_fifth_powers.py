i = 2
valid_numbers = []

while i < 1000000:

    print(i)
    sum_digits_fifth = 0

    for digit in str(i):
        sum_digits_fifth += (int(digit)) ** 5

    if i == sum_digits_fifth:
        print('valid = ', i)
        valid_numbers.append(i)

    i += 1

sum_valid = 0
for number in valid_numbers:
    print(number)
    sum_valid += number
