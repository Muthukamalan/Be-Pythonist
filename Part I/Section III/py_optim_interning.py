# Other Python Implementation: Cpython, Jython, PyPy,...

# Interning: reusing objectts on-demand [-5,256]
# Any time an integer is referenced in that range, py will cached version of the object **Singletons**
# WHY? speed,memory Optimization

# As the py code is compiled, identifiers are interned
#   - variable names
#   - function names
#   - class names


# Peephole:: This is another variety of optimizations that can occur at compile time.
# Peephole optimizations refer to a certain class of optimization strategies Python employs during any compilation phases.

import string
import sys


def foo():
    '''pre-computed all computation'''
    a = 24*60;
    b = (1,2)*5;
    c = 'abc'*3;
    d = 'ab'*11;
    e = 'the quick brown fox' * 5
    f = ['a','b']*3


def boo(e):
    '''converting some mutable to immutable'''
    if e in [1,2,3]:
        pass

def too(e):
    if e in {1,2,3}:
        pass

if __name__=='__main__':
    a = 10;
    b = 10
    print(f"{hex(id(a))}=={hex(id(b))}")

    print(sys.version)


    a = sys.intern("the quick brown lazy fox")
    b = sys.intern("the quick brown lazy fox")
    c = "the quick brown lazy fox"
    print(hex(id(a)), hex(id(b)), hex(id(c)))
    print(a is b)


    print(foo.__code__.co_consts)
    print(boo.__code__.co_consts)
    print(too.__code__.co_consts)

    print(string.ascii_letters)