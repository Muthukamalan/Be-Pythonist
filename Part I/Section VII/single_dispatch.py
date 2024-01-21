# similar to overloading in OOPS
# Py is not statically typed, no overloading not able to distinguish by types

'''Java
class HelloWorld:
    public static void do_something():
        System.out.println("")

    public static void do_something(int x):
        System.out.println("")

    public static void do_something(char*[] x):
        System.out.println("")

'''

'''Python
class Helloworld:
    def do_something(arg):
        print('common call')
            
        if isinstance(arg,int):
            def do_something_int(x):
                pass
            do_something_int(arg)

            
        if isinstance(arg,float):
            def do_something_float(x):
                pass
            do_something_float(arg)
'''

from functools import singledispatch,singledispatchmethod
from numbers import Integral
from collections.abc import Sequence
from typing import Any

@singledispatch
def types(x:Any):
    # serves as base method
    print('NotImplementedError')

@types.register(str)
def types_str(x:str):
    print(f"types is string:::{x}")

@types.register(Integral)
def types_int(x:Integral):
    print(f"types is Integral {str(x)}")

@types.register(Sequence)
def types_seq(x:Sequence):
    print(f"types is Sequence{(x)}")




class Human:
    @singledispatchmethod
    def gender(self,x):
        print("base method")

    @gender.register(Integral)
    def gender_int(self,x:str):
        print('Integral gender')

    @gender.register(list)
    def gender_list(self,x:None):
        print('None gender')



if __name__ == '__main__':
    types(34)
    types('helloworld')
    types([2,43,'hello'])
    types(None)

    h1 = Human()
    h1.gender(2)
    h1.gender((1,2,3))
    h1.gender([1,2,3])
