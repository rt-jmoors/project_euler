words_for_nums = {1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen',
                10: 'ten',
                20: 'twenty',
                30: 'thirty',
                40: 'forty',
                50: 'fifty',
                60: 'sixty',
                70: 'seventy',
                80: 'eighty',
                90: 'ninety',
                100: 'hundred',
                1000: 'thousand'}


def digit_base_components(num):
    """Returns a number written out in words"""

    if num < 10:
        return [num]

    reversed_num = str(num)[::-1]
    output = []
    for num_zeroes, digit in enumerate(reversed_num):
        if digit == '0':
            continue
        elif num_zeroes == 0 and digit != '0':
            if reversed_num[1] != '1':
                output.append(digit)
        elif num_zeroes == 1:
            if digit == '1':
                output.append(digit + reversed_num[0])
            else:
                output.append(digit + '0')
        elif num_zeroes == 2:
            output.extend(('100', digit))
        elif num_zeroes == 3:
            output.extend(('1000', digit))

    output = [int(x) for x in output[::-1]]

    return output


def make_word(components, word_dict):
    """Returns a list of components as a written word"""

    word_list = []
    for component in components:
        word_list.append(word_dict.get(component, None))
        if component == 100 and components[-1] != 100:
            word_list.append('and')

    return ' '.join(word_list)


def count_chars(word):
    """Returns the number of non-blank characters in word"""
    return len(''.join(word.split()))


sum_chars = 0
for i in range(1, 1001):
    word = make_word(digit_base_components(i), words_for_nums)
    num_chars = count_chars(word)
    print(i, ':', word, ':', num_chars)
    sum_chars += num_chars

print('Total letters for numbers:', sum_chars)
