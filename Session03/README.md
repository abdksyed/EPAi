## int -> Inbuilt Class
#### int(x, base=10) . 
An inbuilt Python class, which creates an instance of integer. It returns an integer object. 
Inputs are x and base. **x** can be string or a value directly (like for base10, 255, for base 16 0xff etc) and if string is passed, the base must be given for the given string.
Default: returns zero (**0**) if no arguments are given.

## 'encoded_from_base10' -> Function

A function which accepts three parameters:
number -> int, A number in base 10 format.
base -> int, the base to which the number is to be converted (2<=base<=36)
digit_map -> string, A string of characters in order of its encoding digits.

The functions accepts a number in base 10, a base number to which the number is to converted and the encoding string, which is in order of from 0 to base number, eg: for base 5, encoding can be 'abcde', where 0 is a, 1 is b...e is 5.

Conditions that this function follows:

- If 2 <= *base* <= 36 is not passed, raise ValueError and prints related message.
- If *digit_map* length is not equal to base, i.e. if there are more or less mapping characters than base, than it raises ValueError and prints related message.
- If the *digit_map* have any repeated character raises ValueError and print related message.
- The function doesn't use any math or bin(), hex(), oct() functions. 

The function finally returns the number is given base as per the encoding digit_map.

### code:

    def  encoded_from_base10(number, base, digit_map):  
    
	    if base < 2  or base > 36:
		    raise  ValueError('The base is inavlid. It must be an integer between 2 and 36.')

	    if  len(digit_map) != base:
		    raise  ValueError('The number of characters in your digit_map must be equal to base ')
		    
	    if  len(digit_map) != len(set(digit_map)):
		    raise  ValueError('The characters in your digit_map digit_map are repeating Provide unique characters.')
		    
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

  
## math -> Built in module
It is an inbuilt python module which is designed to provides access to all the mathematical functions defined by the CPython standard.

    import math
    math.pi
    math.floor
    math.sqrt
  

## isclose {math.isclose()} -> Function in math module

Return `True` if the values _a_ and _b_ are close to each other and `False` otherwise.

Whether or not two values are considered close is determined according to given absolute and relative tolerances.

_rel_tol_ is the relative tolerance – it is the maximum allowed difference between _a_ and _b_, relative to the larger absolute value of _a_ or _b_. For example, to set a tolerance of 5%, pass `rel_tol=0.05`. The default tolerance is `1e-09`, which assures that the two values are the same within about 9 decimal digits. _rel_tol_ must be greater than zero.

_abs_tol_ is the minimum absolute tolerance – useful for comparisons near zero. _abs_tol_ must be at least zero.

If no errors occur, the result will be: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.
'absolute' 'tolerance'

## float_equality_testing -> Function
    
    def  float_equality_testing(a, b, rel_tol=1e-12, abs_tol=1e-5):
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
	    
	    if a == b: # short-circuit exact equality
	    return  True
	    
	    return  abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

The function float_equality_testing simulates the math.isclose() function without directing using math module and checks the equality between two floating numbers.

## trunc {math.trunc()} -> Function in math module:
`math.trunc`(_x_)

Return the [`Real`] value _x_ truncated to an [`Integral`](usually an integer).

## manual_truncation_function -> Function

    def  manual_truncation_function(f_num):
	    '''
	    This function emulates python's math.trunc method. It ignores everything after the decimal point.
	    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
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

 The function manual_truncation_function simulates the math.trunc() function without directing using math module and truncates the floating point number to it's integer value.

## round -> Inbuilt Function
Return _number_ rounded to _ndigits_ precision after the decimal point. If _ndigits_ is omitted or is `None`, it returns the nearest integer to its input.

## manual_rounding_function -> Function

    def  manual_rounding_function(f_num):
    
	    '''
	    This function emulates python's inbuild ROUND function.
	    You are not allowed to use ROUND function, but expected to write your one manually.
	    Arguments:
	    f_num -> float, A floating number which is to be rounded off
	    Returns:
	    Rounded Number wihtout decimals.
	    '''
	    
	    if f_num - f_num//1 >= 0.5:
		    return f_num//1 + 1
	    else:
		    return f_num//1


 The function manual_rounding_function simulates the inbuilt round() function, rounding off the floating numbers to the nearest integer values. Eg:
 

	  manual_rounding_function(1.6) = 2
	  manual_rounding_function(-1.35) = -1
	  manual_rounding_function(1.35) = 1
	  manual_rounding_function(-1.55) = -2

 ## rounding_away_from_zero(f_num):
 ### TO-DO

    def  rounding_away_from_zero(f_num):
	    '''
	    This function implements rounding away from zero as covered in the class
	    Desperately need to use INT constructor? Well you can't.
	    Hint: use FRACTIONS and extract numerator.
	    '''
	    return  'NotImplemented'
The function is yet to be implemented and will be implemented in future sessions.
