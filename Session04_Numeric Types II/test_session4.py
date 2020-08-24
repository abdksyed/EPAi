from decimal import Decimal
import decimal
import pytest
import random
import string
import session4
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'Qualean',
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__le__',
    '__lt__',
    '__mul__',
    '__bool__',
    'sqrt',
]

CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_class_repr():
    s = session4.Qualean(0)
    assert 'object at' not in s.__repr__()


def test_class_str():
    s = session4.Qualean(0)
    assert 'object at' not in s.__str__()


def test_sum_100q():
    ran_num = random.choice((-1, 0, 1))
    q = session4.Qualean(ran_num)
    sum_100q = 0
    for _ in range(100):
        sum_100q = q + sum_100q

    assert sum_100q == q*100


def test_sqrt_wtih_Decimal():
    ran_num = random.choice((-1, 0, 1))
    q = session4.Qualean(ran_num)
    if q.num < 0:
        q.num = -q.num
    assert q.__sqrt__() == Decimal(q.num).sqrt()


def sum_1mil_q_close_to_zero():
    sum_1m = 0
    for _ in range(1000000):
        ran_num = random.choice((-1, 0, 1))
        q = session4.Qualean(ran_num)
        sum_1m = q + sum_1m
    assert math.isclose(sum_1m, 0, abs_tol=1e3)


def test_wrong_qualean():
    with pytest.raises(ValueError) as err:
        q = session4.Qualean(3)


def test_qualean_instance():
    q = session4.Qualean(1)
    assert isinstance(q, session4.Qualean)


def test_qualean_value():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)
    assert q1.num >= -1 and q1.num <= 1
    assert q2.num == 0
    assert q3.num >= -1 and q1.num <= 1


def test_num_of_fractional_digits():
    q = session4.Qualean(1)
    assert len(str(q).split(".")[-1]) == 10


def test_repititive_addition_multiplication():
    q = float(session4.Qualean(1).num)
    x = 0
    for _ in range(100):
        x += q
    assert round(float(x), 10) == round(float(q * 100), 10)


def test_sqrt():
    decimal.getcontext().prec = 10
    q = session4.Qualean(1)
    if q.num < 0:
        q.num = -q.num
    assert q.__sqrt__() == Decimal(q.num).sqrt()


def test_add():
    decimal.getcontext().prec = 10
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(-1)
    assert q1 + q2 == q1.num + q2.num


def test_add_instance():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(-1)
    x = q1 + q2
    assert not isinstance(
        x, session4.Qualean), "Added nums can be in [-2, 2], but a session4.Qualean can be in [-1, 1]!"


def test_mul():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    assert (q1 * q2).num == (q1.num * q2.num)


def test_million_qsum():
    x = 0
    for i in range(1000000):
        x = session4.Qualean(random.choice([-1, 0, 1])).num + x
    assert math.isclose(x, 0, abs_tol=1000), ("not nearing to 0", x)


def test_gt():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    if q1.num < 0:
        q1.num = -q1.num
    assert q1 > q2


def test_ge():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(0)
    if q1.num < 0:
        q1.num = -q1.num
    assert q1 >= q2
    assert q2 >= q3


def test_lt():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    if q1.num > 0:
        q1.num = -q1.num
    assert q1 < q2


def test_le():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(0)
    if q1.num > 0:
        q1.num = -q1.num
    assert q1 <= q2
    assert q2 <= q3


def test_eq():
    q1 = session4.Qualean(0)
    q2 = session4.Qualean(0)
    assert q1 == q2

    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    if q1.num == q2.num:
        assert q1 == q2
    else:
        assert q1 != q2


def test_return_False_if_q2_notdefined():
    q1 = session4.Qualean(0)
    assert not (bool(q1) and q2)


def test_return_True_if_q2_notdefined():
    q1 = session4.Qualean(1)
    assert (bool(q1) or q2)


def test_float():
    q = session4.Qualean(1)
    assert isinstance(float(q), float)


def test_inverse():
    q = session4.Qualean(1)
    print(-q)
    print(-(q.num))
    assert (-q).num == -(q.num)


def test_and():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)
    i = 113

    if q1 and q3:
        assert q1.__and__(q3)
    assert not q1.__and__(q2)
    assert not q3.__and__(q2)
    assert not q2.__and__(i)


def test_or():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)
    i = 113

    if q1 or q3:
        assert q1.__or__(q3)
    assert q1.__or__(q2)
    assert q3.__or__(q2)
    if q1:
        assert q1.__or__(i)
