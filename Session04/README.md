# Qualean.

**Qualean** class is inspired by Boolean+Quantum concepts. We can assign it only 3 possible **real** states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number **random.uniform**(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 

Note that the imaginary we are talking about is no where related to complex numbers. At the end, only one number is stored, that is the product. The class after that has no clue of what number did the user enter. This should be clear that a Qualean object can have the final values only between -1 and 1.

Following are the methods of the class `Qualean`.

## _\_init__():

`__init__()`is the constructor and is used to setup the value for the `Qualean` object. Before being assigned, the value should match the conditions of the `Qualean` class.

## _\_eq__ ():

The method `__eq__()` is used to check the equality between two `Qualean` objects. This functionality can be used with the help of '=' operator as well.

## _\_gt__ ():

The method `__gt__()` is used to check if a  `Qualean` object is greater than another `Qualean` object, `number` being the deciding parameter. This functionality can be used with the help of '>' operator as well.

## _\_ge__ ():

The method `__ge__()` is used to check if a  `Qualean` object is greater than or equal to another `Qualean` object, `number` being the deciding parameter. This functionality can be used with the help of '>=' operator as well.

## _\_lt__ ():

The method `__lt__()` is used to check if a  `Qualean` object is less than another `Qualean` object, `number` being the deciding parameter. This functionality can be used with the help of '<' operator as well.

## _\_le__ ():

The method `__le__()` is used to check if a  `Qualean` object is less than or equal to another `Qualean` object, `number` being the deciding parameter. This functionality can be used with the help of '<=' operator as well. 

## _\_repr__():

`__repr__()` method is used to compute the “official” string representation of an object.

## _\_str__:

The `__str__()`method gives the string representation of the object, mainly used by the users. The output of this method is displayed when we use print() to print the object.

## _\_and__():

This method is used to replicate the short circuiting functionality of python with **and** for `Qualean` objects, but cannot be used with `and` keyword as usual.  For using this, we need to explicitly call the `__and__()` method.


## _\_or__():

This method is used to replicate the short circuiting functionality of python with **or** for `Qualean` objects, but cannot be used with `or` keyword as usual.  For using this, we need to explicitly call the `__or__()` method.

## _\_add__():

The method `__add__()` is used to add two `Qualean` objects, but it returns a 'Decimal' value. The sum of two Qualean numbers can be between -2 and 2 but a Qualean can be in between -1 and 1 only. It can be used with the help of '+' operator as well.

## _\_mul__():

The method `__mul__()` is used to multiply two `Qualean` objects, and it returns a `Qualean` type object. It can be used with the help of '*' operator as well.

## _\_neg__():

The `__neg__()` method is used to negate the `Qualean` object. It can w=be used with the '- ' operator as follows:

## _\_float__():

The `__float__()` method gives the floating value of the `Qualean` number, stored in the object.

## _\_bool__():

The `__bool__()` method returns **False** if the value stored in `Qualean` object is 0 otherwise **True**.

## sqrt():

The method `__sqrt__()` returns the square root of the value stored in the `Qualean` object. If the stored value is 0 or positive, it simply gives the Decimal type value as output and if the stored value is negative, it returns a complex number.