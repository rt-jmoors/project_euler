fib_list = [1,2]

# fib_list.append(fib_list[-1]+fib_list[-2])

threshold = 4000000
sum_even_nums = 0

while fib_list[-1] < threshold:
    if fib_list[-1] % 2 == 0:
        sum_even_nums += fib_list[-1]
    fib_list.append(fib_list[-1] + fib_list[-2])

print(len(fib_list))

print(sum_even_nums)
