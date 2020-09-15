from collections import Callable


def scan_fn(scan_len: int) -> 'Function':
    """
    Function to implement closure, encapsulates a function
    that checks whether an input function has a proper docstring,
    with length of atleast 50 characters.
    """
    def check_doc(fn: 'Function') -> 'True or False':
        """
        This is the inner function that actually checks the 
        docstring legth.
        Input: Function for which the docs has to be checked.
        Output: True if doc length > 50 else False
        """
        if not isinstance(fn, Callable):
            raise TypeError("Expected function!")
        if len(fn.__doc__) > scan_len:
            return True
    return check_doc


def fib() -> "Function":
    """
    Function to implement closure, encapsulates a function
    that automatically gives you the next fibonacci number.
    Keeping track of the last fibonacci numbers is the task
    of free variables.
    """
    num_1, num_2 = 1, 1
    count = 0

    def next_fib() -> "Number":
        """
        Returns the next fibonacci number in the sequence.
        """
        nonlocal num_1, num_2, count
        count += 1
        if count <= 2:
            return num_2
        num_1, num_2 = num_2, num_1+num_2
        return num_2
    return next_fib


func_count = {}


def counter() -> "Function":
    """
    Function to implement closure, encapsulates a function
    that keeps tracks of how many times a particular function
    has been called. It updates a global list with count, and
    also mantains a free variable list so as to not let user 
    alter the count.
    """
    counter = {}

    def count(func: 'Function', *args, **kwargs) -> "Function called with provided parameters.":
        """
        Updates and keeps track of the number of times, 
        a function might be called.
        Input: function and *args and *kwargs to be passed
                to the function
        Returns: Returned value from the function, called with
                provided parameters.
        """
        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        func_count[func.__name__] = counter[func.__name__]
        return func(*args, **kwargs)
    return count


def counter_users(user_dict: dict) -> "Function":
    """
    Function to implement closure, encapsulates a function
    that keeps tracks of how many times a particular function
    has been called. It updates a list, provided by user, with count,
    and also mantains a free variable list so as to not let user 
    alter the count.
    """
    counter = {}
    if not isinstance(user_dict, dict):
        raise TypeError('Expected Dictionary')

    def count(func: 'Function', *args, **kwargs) -> "Function called with provided parameters.":
        """
        Updates and keeps track of the number of times, 
        a function might be called.
        Input: function and *args and *kwargs to be passed
                to the function
        Returns: Returned value from the function, called with
                provided parameters.
        """
        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        nonlocal counter
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        user_dict[func.__name__] = user_dict.get(
            func.__name__, 0) + 1
        return func(*args, **kwargs)
    return count
