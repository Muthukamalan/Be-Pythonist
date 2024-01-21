# inner function + free variable
def averager()->float:
    ''' (function) def averager() -> ((numba: Any) -> float '''
    numbers:list =[]
    def add(numba):
        numbers.append(numba)
        return sum(numbers)/len(numbers)
    
    print(f'add function created hex_id:: {hex(id(add))}')
    return add 
    

# Modify free variable
def counter():
    _counter:int = 0 
    def count():
        nonlocal _counter
        _counter+=1
        return _counter
    return count



# shared Extended score
def student():
    _credits = 0

    def test1():
        nonlocal _credits
        _credits+=1
        return _credits
    def test2():
        nonlocal _credits
        _credits+=1
        return _credits
    return test1,test2


# Note
# lambda is just a function
# closure is function + free_variables


# Nested Closure.
# (step: int) -> ((start: Any) -> (() -> Any))
def increment(step:int):
    def inner(start):
        current=start
        def inc():
            nonlocal current   # we're assigning current, if we don't mention nonlocal it'll be local
            current+=step
            return current
        return inc 
    return inner


import time
from typing import Any
class TimerOne:
    def __init__(self) -> None:
        self.start = time.perf_counter()
        time.sleep(4)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return time.perf_counter()-self.start 
    

def timer_two():
    start = time.perf_counter()
    def poll():
        return time.perf_counter() -start
    return poll




COUNTERS={}
def count_functions(fn):
    cnt=0
    def inner(*args:Any,**kwargs:Any):
        nonlocal cnt 
        cnt+=1
        COUNTERS[fn.__name__]=cnt 
        return fn(*args,**kwargs)
    return inner

if __name__=='__main__':

    fn = averager()              # add function created/compiled
    print(f'now, hex_id of averager:: {hex(id(fn))}')                    # fn is closure                  => function + free variable, but HOW? averager scope gone. but it works "Multi-scoped variables"

    # averager.numbers , add.numbers both points intermediate cell that cell points list of values. "double-hop"
    print(fn.__closure__)
    print(fn.__code__.co_freevars)



    # (function) def counter() -> (() -> int)
    c = counter()
    print(c.__closure__)
    print(c.__code__.co_freevars)
    [c() for i in range(2) ]
    print(c())

    # Multiple instance of closures
    d = counter()
    [d() for i in range(20) ]
    print(d())

    # Shared Extended Scopes
    s1 = student()
    # t1, t2 evaluated at the time of calling
    t1,t2 = s1
    t1();t1()
    t2();t2();t2();t2()
    print(t1.__closure__,t2.__closure__)
    print(t1.__code__.co_freevars,t2.__code__.co_freevars)
    

    i = increment(2)  # returns inner
    ii = i(100)       # returns inc
    [ii() for _ in range(10)]
    print(ii())
    print(i.__closure__,ii.__closure__)
    print(i.__code__.co_freevars,ii.__code__.co_freevars)



    # Timer
    t1 = TimerOne()
    print(t1())

    t2 = timer_two()
    time.sleep(4)
    print(t2())



    # COUNTERS
    from operator import add,mul
    count_add = count_functions(add)
    count_mul = count_functions(mul)

    count_add(1,2)
    count_add(3,4)
    count_add(1032,32)
    count_mul(1,43)
    print(COUNTERS)