
# tri = __import__('..problem_18.triangle_modules', fromlist="*")
# from ..problem_18.triangle_modules import *
import sys
sys.path.append(r'C:\project_euler')

from problem_18.triangle_modules import *


triangle_numbers = open('p067_triangle.txt').read()
nums = make_list_integers(triangle_numbers)
triangle = make_triangle(nums)


# Initial conditions to find all path sum combinations
output = triangle[0]
i = 1

while i < len(triangle):

    print('row = ', i)
    output = sum_two_rows(output, triangle[i])
    i += 1

# print(output)

max_paths = []
for combo in output:
    max_paths.append(max(combo))

print('Max path sum = ', max(max_paths))


# doesn't work - memory issue
