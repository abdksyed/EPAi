import pytest
import random
import string
import session5
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter',
    'kmph',
    'km/m/ft/yard',
    'ms/sec/min/hr/day',
    '*args',
    '**kwargs',
    'repetitions',
    'def time_it(fn, *args, repetitions= 1, **kwargs):'
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
            print(c)
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
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_invalid_func_arg():
    with pytest.raises(ValueError):
        session5.time_it(len, repeitions=1)


def test_inalid_keyword_arg():
    with pytest.raises(TypeError):
        session5.time_it(session5.squared_power_list,
                         repeitions=1, invalid_keyword=1)


def test_noarg():
    """
    Checks if missingpositional argument gives value error.
    """
    with pytest.raises(TypeError):
        session5.time_it(session5.speed_converter,
                         repetitions=1, dist='m', time='sec')

    with pytest.raises(TypeError):
        session5.time_it(session5.temp_converter,
                         repetitions=1, temp_given_in='c')

    with pytest.raises(TypeError):
        session5.time_it(session5.polygon_area, repetitions=1, sides=3)

    with pytest.raises(TypeError):
        session5.time_it(session5.squared_power_list,
                         repetitions=1, start=0, end=0)


def test_time_it_squared_power_list():
    res, t, avg_t, tot_t = session5.time_it(session5.squared_power_list, 2,
                                            start=1, end=10, repetitions=1000)
    assert (t > 0 and t < 0.01), 'Improper implementation of squared_power_list function, takes longer than usual to run!'


def test_time_it_polygon_area():
    res, t, avg_t, tot_t = session5.time_it(
        session5.polygon_area, 20, sides=4, repetitions=1000)
    assert (t > 0 and t < 0.01), 'Improper implementation of polygon_area function, takes longer than usual to run!'


def test_time_it_temp_converter():
    res, t, avg_t, tot_t = session5.time_it(session5.temp_converter, 20,
                                            temp_given_in='f', repetitions=1000)
    assert (t > 0 and t < 0.01), 'Improper implementation of temp_converter function, takes longer than usual to run!'


def test_time_it_speed_converter_time():
    res, t, avg_t, tot_t = session5.time_it(session5.speed_converter, 20,
                                            dist='yard', time='sec', repetitions=1000)
    assert (t > 0 and t < 0.01), 'Improper implementation of speed_converter function, takes longer than usual to run!'


def test_invalid_squared_power_list_parameters():
    with pytest.raises(TypeError):
        session5.squared_power_list(10, start="xyz", end=5)
    with pytest.raises(TypeError):
        session5.squared_power_list(10, start=0, end="xyz")
    with pytest.raises(TypeError):
        session5.squared_power_list(1, 2, start=0, end=5)
    with pytest.raises(TypeError):
        session5.squared_power_list("xyz", start=0, end=5)


def test_invalid_temp_converter_argument():
    with pytest.raises(TypeError):
        session5.temp_converter("xyz", temp_given_in='c')

    with pytest.raises(TypeError):
        session5.temp_converter(1, 2, temp_given_in='c')


def test_invalid_temp_converter_temp_type():
    with pytest.raises(ValueError):
        session5.temp_converter(32, temp_given_in='g')

    with pytest.raises(ValueError):
        session5.temp_converter(38, temp_given_in='h')


def test_temp_converter_c_to_f():
    assert session5.temp_converter(
        100, temp_given_in='c') == 212.0, 'temp_converter gives incorrect output'


def test_temp_converter_f_to_c():
    assert session5.temp_converter(
        212, temp_given_in='f') == 100.0, 'temp_converter gives incorrect output'


def test_speed_converter_kmph_to_mps():
    assert session5.speed_converter(
        200, dist='m', time='sec') == 55.55555555555556, 'speed_converter gives incorrect output.'


def test_speed_converter_kmph_to_yardpday():
    assert session5.speed_converter(
        10, dist='yard', time='day') == 262466.4, 'speed_converter gives incorrect output.'


def test_speed_converter_kmph_to_ftpm():
    assert session5.speed_converter(
        5, dist='ft', time='min') == 273.4033333333333, 'speed_converter gives incorrect output.'


def test_triangle_area():
    assert round(session5.polygon_area(
        10, sides=3), 2) == 43.3, 'polygon_area gives incorrect output.'


def test_square_area():
    assert session5.polygon_area(
        10, sides=4) == 100, 'polygon_area gives incorrect output.'


def test_pentagon_area():
    assert round(session5.polygon_area(
        10, sides=5), 2) == 172.05, 'polygon_area gives incorrect output.'


def test_hexagon_area():
    assert round(session5.polygon_area(
        10, sides=6), 5) == 259.80762, 'polygon_area gives incorrect output.'
