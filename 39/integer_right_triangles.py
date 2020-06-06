# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly
# three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

import datetime


def is_triplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False


begin_time = datetime.datetime.now()

p_start = 1000
p_min = 5
a = None
b = None
c = None
solutions = {}

print('Starting')

for p in range(p_start, p_min, -1):
    solutions[p] = []
    print('p:', p)

    for c in range(p - 3, p // 3, -1):

        b = p - c - 1
        a = p - c - b
        # print(c, b, a)

        while b > a:
            if is_triplet(a, b, c):
                solutions[p].append([a, b, c])
                print(solutions[p])

            b -= 1
            a += 1

    if solutions.get(p):
        print(p, ':', solutions.get(p))

max_solutions = 0
for key in solutions.keys():
    if len(solutions[key]) > max_solutions:
        max_solutions = len(solutions[key])
        print(key)

print(datetime.datetime.now() - begin_time)
