# Functions

# import from external module
from math import sqrt


# functions are objects, just like int are object we can assign other variable if we need
# by default, functions will return None values
def greet(name:str)->str:
    '''learn to greet others'''
    return(f'Greetings, {name}')



# The def keyword is an executable piece of code that creates the function (an instance of the function class) and essentially assigns it to a variable name (the function name).
# Note that the function is defined when def is reached, but the code inside it is not evaluated until the function is called.
# This is why we can define functions that call other functions defined later - as long as we don't call them before all the necessary functions are defined.

def fn_1():
    return fn_2()

def fn_2():
    pass


# We also have the lambda keyword, that also creates a new function, but does not assign it to any specific name - instead it just returns the function object - which we can, if we wish, assign to a variable ourselves:
fn_5:callable  = lambda x:x**2





if __name__=='__main__':
    series:list = [1,2,3]
    series_length:int = len(series)
    print(series_length)

    square_of_length:list = sqrt(series_length)
    print(square_of_length)

    say_hi:str = greet('Muthu')   # note that to "call" or "invoke" a functions we need to use the ()

    print(greet)                  # if refers to the function only
    print(say_hi)

    print(fn_1())

    print(fn_5)
    print(fn_5(4))