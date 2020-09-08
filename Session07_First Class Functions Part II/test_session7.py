import pytest
import random
import session7
import os
import inspect
import re
import test_session7

README_CONTENT_CHECK_FOR = [
    'list',
    'comprehensions',
    'map',
    'filter',
    'zip',
    'lambda',
    'operator',
    'partial',
    'reduce'
]


CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You haven't well described your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session7, inspect.isfunction)
    assert len(functions) > 20, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session7, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_fibonacci_positive():
    assert session7.check_fib([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        1, 2, 3, 5, 8], 'One or More number not detected'


def test_fibonacci_empty():
    assert session7.check_fib(
        [14, 234, 44, 345, 745, 1442, 8456, 3452, 463]) == [], 'Wrong Number detected'


def test_add_even_odd_list():
    l1 = [1, 3, 4, 6, 72, 33, 57, 34, 86, 74]
    l2 = [3, 5, 7, 2, 68, 46, 78, 33, 7, 9]
    assert session7.add_even_odd(
        l1, l2) == [11, 67, 93, 83], 'Corresponding Even and Odd only must be added.'


def test_strip_vowel():
    inp_string = 'azzezzizzozzuzz'
    assert session7.strip_vowel(
        inp_string) == 'zzzzzzzzzz', 'Incorrect stripping.'


def test_strip_vowel_empty():
    inp_string = 'kjdklsfjdfvbskljcprjsd'
    assert session7.strip_vowel(
        inp_string) == 'kjdklsfjdfvbskljcprjsd', 'Incorrect stripping.'


def test_relu():
    neurons = [12, 23, -12.2, 13.6, 0, 123.33, -12, -44, -0.0007]
    assert session7.relu(neurons) == [
        12, 23, 0, 13.6, 0, 123.33, 0, 0, 0], "You don't know what ReLU is"


def test_sigmoid():
    neurons = [12, 23, -12.2, 13.6, 0, 123.33, -12, -44, -0.0007]
    assert session7.sigmoid(neurons) == [6.144174602214718e-06, 1.0261879630648827e-10, 0.9999949695696981,
                                         1.2404935411305788e-06, 0.5, 2.7444893312453674e-54, 0.9999938558253978, 1.0, 0.5001749999928542], "You don't know what sigmoid is"


def test_small_char_str():
    small_char_string = 'tsaiz'
    assert session7.shifted_string(
        small_char_string) == 'yxfne', 'Incorrect Shifting'


def test_swear_words():
    inp_text = """But while I was sitting down, I saw something that drove me crazy.
Somebody’d written Fuck you on the wall. It drove me damn near crazy.
I thought how Phoebe and all the other little kids would see it, and how they’d wonder what the hell it meant,
and then finally some dirty kid would tell them—all cockeyed, naturally—what it meant,
and how they’d all think about it and maybe even worry about it for a couple of days.
I kept wanting to kill whoever’d written it. I figured it was some perverty bum that’d
sneaked in the school late at night to take a leak or something and then wrote it on the wall.
I kept picturing myself catching him at it, and how I’d smash his head on the stone steps till
he was good and goddam dead and bloody. But I knew, too, I wouldn’t have the guts to do it. I knew that.
That made me even more depressed."""
    assert session7.swear_word_list(
        inp_text) == ['Fuck', 'damn', 'hell', 'bum'], 'Profanity Check Doomed!'


def test_add_even_odd_reduce():
    num_list = [123, 2343, 32447, 6, 3545]
    assert session7.add_even_odd_reduce(num_list) == 6, 'Check Reduce Function'


def test_big_char():
    small_char_string = 'asdasdqwezxca{we!'
    assert session7.big_char(small_char_string) == '{', 'Check ASCII Codes'


def test_add_3rd():
    num_list = [123, 2343, 3, 32447, 6, 7, 3545]
    assert session7.add_3rd(num_list) == 10, 'Check Reduce Function'


def test_random_num_plates():
    assert len(session7.num_plates) == 15 and len(
        session7.num_plates[13]) == 10 and (session7.num_plates[10][:2] == 'KA')


def test_var_num_plate():
    assert session7.variable_num_plate(
        'DL', 34, 'AZ', 1434) == 'DL34AZ1434', 'Incorrect Number Plate'


def test_var_num_plate_negative():
    with pytest.raises(TypeError):
        session7.variable_num_plate(
            45, 34, 'AZ', 1434) == 'DL34AZ1434', 'Should Raise Type Error'


def test_partial_func():
    assert session7.part_num_plate('KA') == 'KA47AK9999'
    assert session7.part_num_plate('DL') == 'DL47AK9999'
