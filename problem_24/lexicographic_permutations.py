import datetime
import itertools
begin = datetime.datetime.now()
perms = []
for i in itertools.permutations(list('0123456789')):
    perms.append(''.join(i))
perms.sort()
print('millionth permutation = ', perms[999999])
print(datetime.datetime.now() - begin)
