def fib(fib_num):
    """Computes the Fibonacci number given

    Note: Do not use in sequential analysis
    :param fib_num:
    :return:
    """
    if fib_num == 1:
        return 1
    elif fib_num == 2:
        return 2
    else:
        return fib(fib_num - 1) + fib(fib_num - 2)


def fib_fast(x):
    """
    Computes the next Fibonacci number in sequence using current Fibonacci numbers

    :param x: list length 2
    :return: new list with next Fibonacci number in sequence
    """
    if len(x) > 2:
        return
    else:
        return [x[1], x[0] + x[1]]


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


threshold = 4000000
sum_of_even = 0

first = 0
second = 1
fib_nums = [1, 2]

while fib_nums[second] < threshold:
    if is_even(fib_nums[second]):
        sum_of_even += fib_nums[second]

    fib_nums = fib_fast(fib_nums)


print(sum_of_even)
