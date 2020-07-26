import pytest
import random
import string
import session3
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'int',
    'encoded_from_base10',
    'digit_map',
    'ValueError',
    'math',
    'isclose',
    'absolute',
    'relative',
    'tolerance',
    'bin(',
    'hex(',
    'round',
    'truncation',
    'error',
    'equality',
    'zero',
    'away'
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    'math',
    'isclose',
    'bin(',
    'hex(',
    'round(',
    'int(',
    '10.4',
    '-10.4'
    '1.25',
    '-1.25',
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session3)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session3, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_invalid_base_valueerror():
    with pytest.raises(ValueError):
        session3.encoded_from_base10(10, -1, '1234567890')
    with pytest.raises(ValueError):
        session3.encoded_from_base10(10, 1, '012')
    with pytest.raises(ValueError):
        session3.encoded_from_base10(10, 37, '1234567890123456789012345678901234567')

def test_invalid_base_valueerror_provides_relevant_message():
    with pytest.raises(ValueError, match=r".* base .*"):
        session3.encoded_from_base10(10, -1, '1234567890')

def test_innacurate_digit_map_length():
    with pytest.raises(ValueError):
        session3.encoded_from_base10(123123, 16, '0123456789abcde')

    with pytest.raises(ValueError):
        session3.encoded_from_base10(123123, 9, '01234567')


def test_hexadecimal_conversions():
    for _ in range(50):
        r_num = random.randint(0, 32767)
        assert (session3.encoded_from_base10(r_num, 16, '0123456789abcdef').lower() ) == hex(r_num)[2:], f"Your program returned wrong HEX conversions"

def test_negative_hexadecimal_conversions():
    for _ in range(50):
        r_num = random.randint(-32700, -1)
        assert (session3.encoded_from_base10(r_num, 16, '0123456789abcdef').lower() ) == '-' + hex(r_num)[3:], f"Your program returned wrong HEX conversions"


def test_repeating_digits_in_digit_map():
    with pytest.raises(ValueError):
        session3.encoded_from_base10(10, 10, '0123401234')

def test_repeating_digits_valueerror_provides_relevant_message():
    with pytest.raises(ValueError, match=r".* repeating .*"):
        session3.encoded_from_base10(10, 10, '012AB012ab'), 'Something is fishy! You are not using word "repeating" while talking about an error releated to "repeating" alphanumerics!!'

def test_float_equality_testing():
    for _ in range(10000):
        scale = random.randint(1, 1000000)
        a = random.uniform(-1.5, 1.6)
        a, b = a * scale, a * scale - a / scale
        assert session3.float_equality_testing(a, b) == math.isclose(a, b, rel_tol = 1e-12, abs_tol=1e-05), 'Aap jis number se sampark karna chahte hai, woh is samay uplabdh nahi hai, kripya thodi der baad prayas karein. The numbers you are trying to check right now are not equal, please try again later'

def test_things_not_allowed():
    code_lines = inspect.getsource(session3)
    for word in CHECK_FOR_THINGS_NOT_ALLOWED:
        assert word not in code_lines, 'Have you heard of Pinocchio?'

def test_fraction_used_or_not():
    code_lines = inspect.getsource(session3)
    assert 'fractions' in code_lines, 'Fractions not used! You must use fractions'
    assert 'import' in code_lines, 'You have not imported fractions!'

def test_manual_truncation_function():
    for _ in range(100):
        f_num = random.uniform(-100, 100)
        assert session3.manual_truncation_function(f_num) == math.trunc(f_num), 'Just because you are not able to fix this truncation error, SkyNet is going to rule the earth!'

def test_manual_rounding_function():
    for f_num in [1.25, 1.35, -1.25, -1.35]:
        assert session3.manual_rounding_function(f_num) == round(f_num), 'Terminator after looking at your code: I will be back! He will come back when you fix your rounding errors.'


def test_functions_for_zero():
    assert session3.float_equality_testing(0.0, 0.0), 'How can zero be not equal to zero?'
    assert session3.manual_truncation_function(0.0) == 0, 'Tuncation of 0 should be zero'
    assert session3.manual_rounding_function(0.0) == 0, 'Zero can only be rounded off to zero'

