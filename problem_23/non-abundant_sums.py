# non-abundant sums - problem 23


def find_divisors(number):
    divisors = []
    for i in range(1, number//2 + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def is_abundant(divisors, number):
    if sum(divisors) > number:
        return True
    return False

lower = 1
upper = 28124
# upper = 100
abundant_list = []
for i in range(lower, upper):
    if is_abundant(find_divisors(i), i):
        # print(i)
        abundant_list.append(i)


# print(abundant_list)
print(len(abundant_list))


sum_pairs = []

i = 0
while i < len(abundant_list):
    j = i
    while j < len(abundant_list):
    # print('i, j:', i, ', ', j)
        pair_sum = abundant_list[i] + abundant_list[j]
        # if pair_sum not in sum_pairs:
        sum_pairs.append(pair_sum)
            # print(sum_pairs[-1])
        j += 1
    i += 1

print('length sum_pairs = ', len(sum_pairs))

unique_sum_pairs = set(sum_pairs)

print('unique_sum_pairs length = ', len(unique_sum_pairs))


cumulative_sum = 0
for i in range(1, 28124):
    if i in unique_sum_pairs:
        # print('sum of 2 abundant numbers: ', i)
        continue
    else:
        # print('i: ', i)
        cumulative_sum += i
        # print('cumulative_sum = ', cumulative_sum)

print('Cumulative sum of numbers which are not a combination of abundant pairs: ', cumulative_sum) 


