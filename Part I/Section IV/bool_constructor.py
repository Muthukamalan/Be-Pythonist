# bool class is subclass of int
# constants are defined:: True and False

# They are singleton objects of type bool
#   - already defined with pre-defined values
#   - retains same memory will program dies

from fractions import Fraction
from decimal import Decimal


if __name__=='__main__':
    print(issubclass(bool,int))
    print(type(True), id(True), int(True))
    print(type(False), id(False), int(False))


    # singleton object
    print(id(True), id(1 < 2))


    # any number can cast to bool
    print(bool(0), bool(-1), bool(100))  # Truthyness

    print(bool(10), bool(1.5), bool(Fraction(3, 4)), bool(Decimal('10.5')))
    print(bool(0), bool(0.0), bool(Fraction(0,1)), bool(Decimal('0')), bool(0j))

    print(bool([1, 2, 3]), bool((1, 2, 3)), bool('abc'), bool(1j))
    print(bool([]), bool(()), bool(''))


    print(bool({'a': 1}), bool({1, 2, 3}))
    print(bool({}), bool(set()))

    print(bool(None))



    # Be Aware of how we use precedence.
    print(True or True and False)
    # is equivalent to 
    print(True or (True and False))
    # not
    print((True or True) and False)    


    # 
    print(bool(None))
    print(bool(not None))

    # The **is** and **is not** operators will work with any data type since they are comparing the memory addresses of the objects (which are integers)
    # The **in** and **not in** operators are used with iterables

    print(Decimal('0.1') == Fraction(1, 10))