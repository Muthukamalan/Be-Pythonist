# callable
# A callable is an object that can be called (using the **()** operator), and always returns a value.
# Always returns a value

import string
from random import random
from decimal import Decimal
from typing import Any


shuffled_letters:list =  sorted(list(string.ascii_letters),key=lambda _:random(),reverse=True)

class MyFunc:
    def __init__(self) -> None:
        pass

# But,
class Testimonial:
    def __init__(self) -> None:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> None:
        print(f"args={args}, kwargs={kwds}")


if __name__=='__main__':
    print(callable(print))
    print(callable(shuffled_letters.append))
    print(callable(Decimal))

    foo = MyFunc()
    print(callable(foo))

    t = Testimonial()
    print(callable(t))
    t(1,2,3,4,kw1=2,plot='rug')