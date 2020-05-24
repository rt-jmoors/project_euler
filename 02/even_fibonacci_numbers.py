from fib import *

threshold = 4000000
sum_of_even = 0

fib_nums = [1, 2]

while fib_nums[1] < threshold:
    if is_even(fib_nums[1]):
        sum_of_even += fib_nums[1]

    fib_nums = fib_fast(fib_nums)


print(sum_of_even)
