# Project file for project 4 Largest Palindrome Product 

# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99. 

# Find the largest palindrome made from the product of two 3-digit numbers.
three_digits = [*range(1000, 99, -1)]

num_found = False
for x in three_digits:
    for y in three_digits:
        product = str(x * y)
        if product == product[::-1]:
            num_found = True
            print(product)
            break
    if num_found:
        break
