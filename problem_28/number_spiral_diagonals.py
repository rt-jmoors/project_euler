spiral_num = 1
sum_diagonal = 1
n = 1

while n <= 500:
    width = 1 + 2 * n
    print('width:', width)
    for i in range(4):
        spiral_num += width - 1
        print('\t spiral: ', spiral_num)
        sum_diagonal += spiral_num
    n += 1

print(sum_diagonal)
