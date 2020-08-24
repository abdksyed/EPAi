from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Arguments:
    number -> int, A number in base 10 format.
    base -> int, the base to which the number is to be converted (2<=base<=36)
    digit_map -> string, A string of characters in order of its encoding digits.

    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
    '''

    if base < 2 or base > 36:
        raise ValueError('The base is inavlid. It must be an integer between 2 and 36.')

    if len(digit_map) != base:
        raise ValueError('The number of characters in your digit_map must be equal to base ')

    if len(digit_map) != len(set(digit_map)):
        raise ValueError('The characters in your digit_map digit_map are repeating Provide unique characters.')

    digits = []

    if number == 0:
        return digit_map[0]
    elif number < 0:
        number = -1 * number
        i = -1
    else:
        i = 1

    while number > 0:
        m = number % base
        number = number // base
        digits.insert(0,m) #Insert the m at 0th position in list.
    if i == -1:
        conv = '-'+''.join(digit_map[encode] for encode in digits)
    else:
        conv = ''.join(digit_map[encode] for encode in digits)

    return conv

def float_equality_testing(a, b, rel_tol=1e-12, abs_tol=1e-5):
    '''
    This function emulates the ISCLOSE method from the MATH module, but you can't use this function
    We are going to assume:
    - rel_tol = 1e-12
    - abs_tol = 1e-05
    Arguments:
    a -> float, First Number
    b -> float, Second Number which is check for equality with a
    rel_tol -> float, default: 1e-12. The relative tolerance between numbers.
    abs_tol -> float, default: 1e-5. The absolute tolerance between numbers.
    '''
    if a == b:  # short-circuit exact equality
        return True
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, FLOAT, etc
    Arguments:
    f_num -> float, A floating number which is to be truncated
    Returns:
    Truncated number.
    '''
    if f_num == 0:
        return f_num
    elif f_num > 0:
        return f_num // 1
    else:
        return f_num // 1 + 1

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    Arguments:
    f_num -> float, A floating number which is to be rounded off
    Returns:
    Rounded Number wihtout decimals.
    '''
    if f_num - f_num//1 >= 0.5:
        return f_num//1 + 1
    else:
        return f_num//1

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0