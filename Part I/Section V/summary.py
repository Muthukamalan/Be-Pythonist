# Positionals only: no extra positionals, no defaults (all position req)
def func1(a,b):
    print(f"a={a}, b={b}")
    print('-'*50)

# Positionals only: no extra positionals, defaults(some defaults optional)
def func2(a,b='world', c=10):
    print(f"a={a}, b={b}, c={c}")
    print('-'*50)

# Positionals only: extra positionals, no defaults (all positionals required)
def func3(a,b,*args):
    print(f"a={a}, b={b}, args={args}")
    print('-'*50)

# Keywords only: no defaults (all keyword args required)
def func4(*args,a,b):
    print(f"args={args}, a={a}, b={b}")
    print('-'*50)

# Keywords Only: no positionals, some defaults (not all keyword args required)
def func5(*args,a='hello',b='world'):
    print(f"args={args}, a={a}, b={b}")
    print('-'*50)

# Keywords and Positionals: some positionals (no defaults), keywords (no defaults)
def func6(a,b,*args,c,d):
    print(f"a={a}, b={b}, args={args}, c={c}, d={d}")
    print('-'*50)

# Keywords and Positionals: some positional defaults
def func7(a, b=2, *args, c, d=4):
    print(f"a={a}, b={b}, args={args}, c={c}, d={d}")
    print('-'*50)

# Keywords and Positionals: no extra positionals, extra keywords
def func8(a, b, *args, c, d=4, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, d={d}, kwargs={kwargs}")
    print('-'*50)

    
# Keywords and Positionals: only extra positionals and extra keywords
def func9(*args, **kwargs):
    print(f"args={args}, kwargs={kwargs}")
    print('-'*50)


# GOTCHA
import time
from datetime import datetime
def logger(msg='',dt=datetime.today()):   # evaluated at compile time, not when call it.
    print(msg, "and time=",dt)

if __name__=='__main__':
    # func1(2,3)
    # func2(19,c=23)
    # func3(1,2,3,4,5,6,7,8,9,10)
    # func4(1,2,4,a=5,b=10)
    # func5(1,2,3,4,5,a='hello',b=100)
    # func6(1,2,4,5,6,7,8,c='hello',d='world!')
    # func7(1,23,4,2,3,c='hello world')
    # func8(1,2,10,20,30,c=3,x='hello',y='world')
    # func9(10,20,30,40,50,hello="hello",world="world!!")


    # Both returns same time, WHY?
    logger('hello world')
    time.sleep(10)
    logger('bye world!')
    # dt defines at compile time. not when call it