limit = 1000
sum_total = 0
if limit > 0:
    for x in range(0, limit):
        if x % 3 == 0 or x % 5 == 0:
            sum_total += x
print(sum_total)