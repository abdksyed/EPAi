from typing import List
from memory_profiler import memory_usage
import time
import gc

#TASK:
# Here in this code we will be leaking memory because we are creating cyclic reference. 
# Find that we are indeed making cyclic references.
# Eventually memory will be released, but that is currently not happening immediately.
# We have added a function called "clear_memory" but it is not able to do it's job. Fix it. 
# Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that
# this code is sub-optimal.

class Something(object):
    '''A Dummy Class which is used to create Cyclic References'''

    def __init__(self):
        super().__init__()
        self.something_new = None

    def __repr__(self):
        return f'Hey You Found Something'


class SomethingNew(object):
    '''Anothe Dummy Class which is used to create Cyclic Reference.
    Arguments:
    i -> int -> default= 0. Just a variable.
    Something -> Class Object -> default= None'''

    def __init__(self, i: int = 0, something: Something = None):
        super().__init__()
        self.i = i
        self.something = something

    def __repr__(self):
        return f'Hey You Again Found Something New'


def add_something(collection: List[Something], i: int):
    '''A Function which takes a list and int as input.
    Creates Cyclic References using Two Class Objects and append
    it to the main list.'''

    something = Something()
    something.something_new = SomethingNew(i, something)
    collection.append(something)


def reserved_function():
    '''to be used in future if required'''
    pass

def clear_memory(collection: List[Something]):
    '''A function which take a list as input and performs clearing 
    the list and clearing all cyclic references using garbage collector.'''

    collection.clear() #Empties the Entire List
    gc.collect() #Run Garbage Collector and removes all Cyclic References


def critical_function():
    '''This Function will runs the above *add_something* fucntion for 1024*128(131,072) times
    and create tons of cyclic references loading the memory.
    At last calling clear_memory to clean up the memory.'''

    collection = list() 
    for i in range(1, 1024 * 128):
        add_something(collection, i)
    clear_memory(collection)


# Here we are suboptimally testing whether two strings are exactly same or not
# After that we are trying to see if we have a particular character in that string or not
# Currently the code is suboptimal. Write it in such a way that it takes 1/10 the current time

# DO NOT CHANGE THIS PROGRAM
def compare_strings_old(n):
    '''The function has two very long strings with whitesapces, so it is not interned.
	The function take a number *n* and checks whether the two strings are exact same
	or not for n times. (Here exactly same refers to same value and in same location).
	And also, the second part in the code check for the letter 'd' in the list of 
	characters of the string for n times.'''

    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass

# YOU NEED TO CHANGE THIS PROGRAM
def compare_strings_new(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a is b:
            pass
    char_list = set(a)
    for i in range(n):
        if 'd' in char_list:
            pass