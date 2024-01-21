import time
from functools import wraps
from typing import Any
from datetime import datetime,timezone


def timed(fn):
    @wraps(fn)
    def inner(*args:Any,**kwargs:Any):
        start:float = time.perf_counter()
        result = fn(*args,**kwargs)
        end:float = time.perf_counter()   
        elapsed:float = end - start
        
        args_:list    = [str(_) for _ in args]
        kwargs_:list  = ['{0}-{1}'.format(k,v) for k,v in kwargs.items()]
        all_args:list = args_+kwargs_
        args_str:str  = ''.join(all_args)
        print('{0}({1} took {2:.6f}s to run.)'.format(fn.__name__,args_str,elapsed))
        return result
    return inner


def logged(fn):
    @wraps(fn)
    def inner(*args,**kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args,**kwargs)
        print('{0}: called {1}'.format(fn.__name__,run_dt))
        return result
    return inner




def calculate_recursive_fib(n:int)->int: return 1 if n<=2 else calculate_recursive_fib(n-1)+calculate_recursive_fib(n-2)


@timed
def fib_recursion(n:int): return calculate_recursive_fib(n)


@timed
def fib_loop(n:int)->int:
    fib_1:int =1     # 0+1
    fib_2:int =1     # (0+1) + 1
    for i in range(3,n+1):
        fib_1,fib_2 = fib_2, (fib_1+fib_2)
    return fib_2



@logged
def foo():
    pass

@timed
@logged
def boo():
    pass


# Memoization
# Write efficient Recursive-Fib by adding + space
class Fib:
    def __init__(self) -> None:
        self.cache = {1:1,2:1}

    def __call__(self, n:int,*args: Any, **kwds: Any) -> Any:
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]


def fibanocci():
    cache:dict ={1:1,2:1}
    def innner(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = innner(n-1)+innner(n-2)
        return cache[n]
    return innner



def memoize(fn):
    cache = dict()
    @wraps(fn)
    def inner(*args):
        if args not in cache:
            cache[args]=fn(*args)
        return cache[args]
    return inner


@memoize
def memoize_fib(n:int):
    print('calculating fib{}'.format(n))
    return 1 if n<3 else memoize_fib(n-1)+memoize_fib(n-2)

@memoize
def memoize_fact(n:int):
    print('calculating fact {}'.format(n))
    return 1 if n<2 else n*memoize_fact(n-1)


if __name__ == '__main__':
    n:int = 30
    print(fib_recursion(n))
    print(fib_loop(n))

    foo()
    boo()

    f1 = Fib()
    print(f"fibanocci of {n} is {f1(n)}")

    f2 = fibanocci()
    print(f"fibanocci of {n} is {f2(n)}")


    memoize_fact(6)
    memoize_fact(7)