import pytest
import inspect
from test_utils import *
import re

import session1


WIDTH = 10
HEIGHT = 20
def test_fourspace_equal():
    assert fourspace(session1) == False, 'Not all spaces before lines are a multiple of 4!'

def test_function_names():
    assert function_name_had_cap_letter(session1) == False, "One of your function has a capitalized alphabet!"

def test_rectangle_repr():
    r = session1.Rectangle(WIDTH, HEIGHT)
    assert r.__repr__() == f'Rectangle({WIDTH}, {HEIGHT})', 'The representation of the Rectangle object does not meet expectations'

def test_rectangle_str():
    r = session1.Rectangle(WIDTH, HEIGHT)
    assert r.__str__() == f'Rectangle: width={WIDTH}, height={HEIGHT}', 'The print of the Rectangle object does not meet expectations'

def test_rectangle_area():
    r = session1.Rectangle(WIDTH, HEIGHT)
    assert r.area() == WIDTH*HEIGHT, "Your Rectangle Class does not know how to calculate rectangle's area!"

def test_rectangle_perimeter():
    r = session1.Rectangle(WIDTH, HEIGHT)
    assert r.perimeter() == 2 * ( WIDTH + HEIGHT ), "Man! Rectangle's perimeter is wrong, consider changing your profession."

def test_rectangle_negative_sides():    
    with pytest.raises(ValueError) as e_info:
        r = session1.Rectangle(-WIDTH, -HEIGHT)

def test_rectangle_equality():
    r1 = session1.Rectangle(WIDTH, HEIGHT)
    r2 = session1.Rectangle(WIDTH, HEIGHT)
    assert r1 == r2, "Rectangles with same w and h must be equal!"

def test_rectangle_comparison():
    r1 = session1.Rectangle(WIDTH, HEIGHT)
    r2 = session1.Rectangle(WIDTH*2, HEIGHT)
    assert r1 < r2, "r2 must be larger than r1"

def test_rectangle_comparison_with_non_rectangle():
    with pytest.raises(NotImplementedError) as e_info:
        r1 = session1.Rectangle(WIDTH, HEIGHT)
        r2 = "Rectangle"
        r1 < r2
