# Champernowne's constant


irrational_decimal = ""
counter = 1
while len(irrational_decimal) < 1000000:
    irrational_decimal += str(counter)
    counter += 1



index_list = [1, 10, 100, 1000, 10000, 100000]
output = 1
for index in index_list:
    print(irrational_decimal[index-1])
    output *= int(irrational_decimal[index-1])

print(output)


## alternative

s = ''.join([str(x) for x in range(0, 10000)])
