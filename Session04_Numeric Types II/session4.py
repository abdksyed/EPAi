from decimal import Decimal, ROUND_HALF_EVEN
import math
import random
import sys


class Qualean(object):
    '''
    Qualean(x) -> Imaginary Number ranging from -1 to 1.

    Convert a real state of either -1, 0 or 1 into an imaginary
    state of any number ranging between -1 to 1.
    Qualean = input * random.uniform(-1,1)

    Methods defined here:

    __abs__(self)
        abs(self.num)

    __add__(self, other)
        Return self.num + other.num.

    __and__(self, other)
        Return self.num & other.num.

    __bool__(self)
        self != 0

    __eq__(self, other)
        Return self.num == other.num.

    __float__(self)
        float(self.num)

    __ge__(self, other)
        Return self.num >= other.nun.

    __gt__(self, other)
        Return self.num > other.nun.

    __invertsign__(self)
        Return -self

    __le__(self, other)
        Return self.num <= other.nun.

    __lt__(self, other)
        Return Return self.num < other.nun.

    __mul__(self, other)
        Return self.num * other.num.

    __ne__(self, value, /)
        Return self!=value.

    __or__(self, value, /)
        Return self|value.

    __repr__(self, /)
        Return repr(self).

    __round__(self, prec, rounding)
        Arguments:
        prec: Precision to be rounded
        rounding: Type of Rounding
        Rounding options include ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR,
        ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, and ROUND_05UP

        Return Quantized Rounding.

    __str__(self, /)
        Return str(self).

    __sub__(self, other)
        Return self-other.

    sizeof(self)
        Returns size in memory, in bytes.

    conjugate(self)
        Returns the complex conjugate.
    '''

    def __init__(self, input: int):
        if not isinstance(input, (int, float)):
            raise TypeError(
                f"unsupported type {type(input)}. Please enter one among (-1, 0, 1)")
        if input not in (1, -1, 0, -1.0, -0.0, 1.0):
            raise ValueError(
                f'Invalid INput, Input must be 1 or 0 or -1, you entered {input}')
        self.input = input
        self.num = Decimal(self.input * random.uniform(-1, 1))
        self.num = self.num.quantize(
            Decimal('0.0000000001'), rounding='ROUND_HALF_EVEN')

    def __abs__(self):
        return abs(self.num)

    def __and__(self, other):
        return bool(self.num and other.num)

    def __or__(self, other):
        return bool(self.num or other.num)

    def __add__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return self.num + other

        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for +: Can not add 'Qualean' and {type(other)}")

        return self.num + other.num

    def __sub__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return self.num - other

        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for -: Can not subtract 'Qualean' and {type(other)}")

        return self.num - other.num

    def __eq__(self, other):
        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for ==: Can not equate 'Qualean' and {type(other)}")

        return self.num == other.num

    def __ne__(self, other):
        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for !=: Can not equate 'Qualean' and {type(other)}")

        return self.num != other.num

    def __float__(self):
        return float(self.num)

    def __Decimal__(self):
        return self.num

    def __ge__(self, other):
        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for >=: Can not compare 'Qualean' and {type(other)}")

        return self.num >= other.num

    def __gt__(self, other):
        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for >: Can not compare 'Qualean' and {type(other)}")

        return self.num > other.num

    def __le__(self, other):
        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for <=: Can not compare 'Qualean' and {type(other)}")

        return self.num <= other.num

    def __lt__(self, other):
        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for <: Can not compare 'Qualean' and {type(other)}")

        return self.num < other.num

    def __invertsign__(self):

        return self.num.copy_negate()

    def __neg__(self):

        neg_q = Qualean(0)
        neg_q.num = -self.num
        return neg_q

    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return self.num * other

        if not isinstance(other, Qualean):
            raise TypeError(
                f"unsupported operand type(s) for *: Can not multiply 'Qualean' and {type(other)}")

        mul_q = Qualean(0)
        mul_q.num = self.num * other.num
        return mul_q

    def __round__(self, prec=1e-10, rounding='ROUND_HALF_EVEN'):

        return self.num.quantize(Decimal(str(prec)), rounding=rounding)

    def __sqrt__(self):
        if self.num >= 0:
            return self.num.sqrt()

        return complex(0, (-1*self.num).sqrt())

    def __bool__(self):

        return self.num != 0

    def __repr__(self):
        return f'Hey!, I am a Qualean with value {self.num} and I am very VOLATILE, so every time you call me I CHANGE'

    def __str__(self):
        return str(self.num)

    def sizeof(self):

        return sys.getsizeof(self.num)

    def conjugate(self):

        return complex(0, self.num)


# num = random.choice([-1, 0, 1])
# q = Qualean(1)
# print('The Qualean: ', q)
# sum_100 = 0
# for i in range(100):
#     sum_100 = q.num + sum_100
# print('Sum Test: ', sum_100 == q.num*100)

# if q.num < 0:
#     q.num = q.__invertsign__()
# print('Square Root Test: ', q.__sqrt__() == Decimal(q.num).sqrt())

# sum_1m = Qualean(0).num
# for _ in range(1000000):
#     random_num = random.choice([-1, 0, 1])
#     q = Qualean(random_num)
#     sum_1m += q.num
# print('Sum Close to Zero', math.isclose(0, sum_1m, abs_tol=1e3))

# t1 = Qualean(0)
# t2 = Qualean(1)
# print(bool(t1 and this_doesnt_exist))
# print(bool(t2 or this_also_doesnt_exist))
