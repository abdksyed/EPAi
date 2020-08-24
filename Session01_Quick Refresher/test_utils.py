import re
import inspect


def fourspace(module_name):
    r''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(module_name)
    spaces = re.findall('\n(.+?)[a-zA-Z0-9]', lines)
    for space in spaces:
        if len(space) % 4 > 0 and len(space) != 1:  # 1 in case new fn or cls start after \n
            print(space)
            return True
    return False


def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False
