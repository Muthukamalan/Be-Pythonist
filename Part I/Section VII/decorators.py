# Note:
# Lambda is just a function
# Functions defined inside another function can access the outer (nonlocal) variables
# Closure = function + free accessible variable
# Decorators = take function wraps with extra functionality but works as same.

from operator import add,mul,sub
from functools import wraps
from typing import Any
from inspect import getsource,signature,get_annotations

def counter(fn):
    count = 0
    
    def inner(*args, **kwargs)->Any:
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


# shorthand to call decorator
@counter
def sub(a:int,b:int)->int:
    ''' subtract lesser number from greater number  '''
    if a>b:
        return a-b
    return b-a



def wrap_counter(fn):
    count = 0
    
    @wraps(fn)
    def inner(*args,**kwargs):
        nonlocal count 
        count+=1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args,**kwargs) 
    # inner.__name__ = fn.__name__
    # inner.__doc__  = fn.__doc__
    return inner

@wrap_counter
def is_positive(b:int)->bool:
    '''check number is greater than or equal to one else return False'''
    if b>=1:
        return True
    return False
    
    


if __name__=='__main__':
    print(f"hex id of add::{hex(id(add))}, mul:: {hex(id(mul))}")

    print(f"name from operator module  ::{ add.__name__}")
    print(f"params of add:: {signature(add).parameters}")
    print(f"signature of add:: {signature(add)}")





    add = counter(add)
    print(f"hex id of add::{hex(id(add))}, mul::{hex(id(mul))}")
    print(f"after modified by decorator::{ add.__name__}")
    print(f"params of add:: {signature(add).parameters}")
    print(f"signature of add:: {signature(add)}")


    add(1,2)
    mul(13,2)
    sub(4,3)

    

    is_positive(0)
    is_positive(323)
    print(f"decorator is_positive::{ is_positive.__name__}")
    print(f"params of is_positive:: {signature(is_positive).parameters}")
    print(f"signature of is_positive:: {signature(is_positive)}")


    
    