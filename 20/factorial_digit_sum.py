
product = 1
i = 100

while i > 0:
    product *= i
    i -= 1

sum = 0
for elem in str(product):
    sum += int(elem)

print(sum)