# problem 26 reciprocal cycles

recurring = {}
quot_list = []
dividend = 10
d = 1
max_recurring = 0
while d < 1000:
    if dividend % d in quot_list:
        # have found recurring cycle in decimal part
        recurring[d] = len(quot_list)
        if recurring[d] > max_recurring:
            max_d = d
            max_recurring = recurring[d]
        d = d + 1
        quot_list = []
        continue
    elif dividend % d == 0:
        # number not recurring - divides evenly
        d = d + 1
        continue
    else:
        quot_list.append(dividend % d)
        dividend = quot_list[-1] * 10


print('value of d: ', max_d, 'recurring length: ', recurring[max_d])
