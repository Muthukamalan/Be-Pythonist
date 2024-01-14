# The ``float`` class can be used to represent real numbers. 64 bits


# sign             -> 1bit
# exponent         -> 11 bits
# significant digit-> 52 bits

# 1.5E-5

from fractions import Fraction
from math import isclose
if __name__=='__main__':
    # help(float)

    print(float(10))
    print(format(0.132,'.24f'))
    print(float(Fraction('22/7')))

    x = .1 + .1 + .1
    y = .3
    print('x --> {0:.25f}'.format(x))
    print('y --> {0:.25f}'.format(y))
    print(x == y)
    print(round(x, 5) == round(y, 5))
    print(isclose(x,y,rel_tol=0.00000000000000000001))  # relative tolerance
    print(isclose(x,y,abs_tol=0.001))                   # absolute tolerance



    # truncation
    # returns integer portion of the number

    # floor
    # a//b == floor(a/b)

    # ceiling
    # ceil of a number is the smallest ineger greater than (or equal) to the number


    # rounding
    # rounding upto some specific number of decimals