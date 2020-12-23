# 1000-digit Fibonacci number

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


fib_list = [1, 1]
while len(str(fib_list[-1])) < 1000:
    fib_list.append(fib_list[-2] + fib_list[-1])

print('index = ', len(fib_list))
print('length digits = ', len(str(fib_list[-1])))
print('value = ', fib_list[-1])
