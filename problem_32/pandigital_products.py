
def is_pandigital(num):
    """Determines if a number is pandigital or not

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
    5 pandigital.
    """
    digits = set(str(num))
    for digit in digits:
        if int(digit) > len(str(num)):
            return False
        elif str(num).count(digit) > 1:
            return False
    return True
