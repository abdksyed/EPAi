# Assignemt 8 - Scopes and Closures

## Topics Covered:

* Global and Local Scope

* Non Local Scopw

* Closures

* Closure Applications

## Link to Class Notebook (along with Notes)

[Class Notebook with extra Notes.](https://github.com/abdksyed/EPAi/blob/master/Session08_Scopes and Closures/notebooks/Session08_Notes.ipynb)

# Scopes and Closures

The main goal here is to implement nested functions and closures. Walking through the use cases, one will realize that closures are an effective way to implement certain functionalities that require some data abstraction and also be used in place of classes for some use cases. This also helps in reducing the memory overhead.

## Scan Fucntion (Docstring Length Check) 

The idea here is to check if a given function has proper docstring, whose character count should be at least 50. The value 50 is passed as a free variable and the functionality is implemented through closure.

```python
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
        if len(fn.__doc__) > scan_len:
            return True
    return check_doc
```

## Next Fibonacci!!

Here, we have a function which is used to generate Fibonacci numbers, by making use of closure. The free variables hold the record of what was the last fetched fibonacci number and accordingly, whenever the respective function is called, it returns the next number in the sequence.

```python
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
```

## Function call counter

Here, we have a global dictionary, which holds the number of times a particular function is called. There is no restriction to the function which might be called. If a function is called for the first time, it is added to the dictionary. The task was to implement this for add, mul, div functions, but this has been extended to accommodate any function that might be called.

Take a note that, apart from the global dictionary, we also have a dictionary as free variable to internally keep track of the count. This is to make correct updates of the function call counts, even if the user alters the global dictionary. As previous functions, we make use of closure to implement these functionalities.

```python
# Global dictionary that holds the number of times a particular function is called.
func_count = {}
def counter():
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
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        func_count[func.__name__] = counter[func.__name__]
        return func(*args, **kwargs)
    return count
```

## Function call counter - user differentiable

This call counter implementation is also similar to the previous one, except that this time the user is supposed to provide a dictionary explicitly and all the count updates would be made to it instead of that global dictionary in the previous case.

```python
def counter_users(user_dict: dict) -> "Function":
    """
    Function to implement closure, encapsulates a function
    that keeps tracks of how many times a particular function
    has been called. It updates a list, provided by user, with count,
    and also mantains a free variable list so as to not let user 
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
        nonlocal counter
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        user_dict[func.__name__] = user_dict.get(
            func.__name__, 0) + 1
        return func(*args, **kwargs)
    return count
```