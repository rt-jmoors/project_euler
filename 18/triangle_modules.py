import re


def sum_two_rows(top, bottom):
    output = [[] for x in range(0, len(bottom))]

    for i in range(0, len(top)):
        for j in range(i, i + 2):
            if isinstance(top[i], list):
                for elem in top[i]:
                    output[j].extend([elem + bottom[j]])
            else:
                output[j].extend([top[i] + bottom[j]])

    return output


def make_list_integers(num_list):
    """Takes a string of 2-digit integer values separated by a space, and returns them as a list of integers"""

    two_digit_regex = re.compile(r'\d{2}')
    nums = []
    for number in two_digit_regex.findall(num_list):
        nums.append(int(number))
    return nums


def make_triangle(numbers):
    """Takes a list of numbers, and returns a continuously growing triangle"""

    row_count = 1
    start_index = 0
    i = 1
    triangle = []
    while start_index < len(numbers):
        end_index = start_index + i
        triangle.append(numbers[start_index:end_index])
        start_index = end_index
        i += 1
    return triangle
