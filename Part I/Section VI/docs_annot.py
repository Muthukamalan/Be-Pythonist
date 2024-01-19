# Docstring
# when we call help(obj) return info about object. nothing with code or optimization.


# Annotation
# annotations are stored in the `__annotations__` property - a dictionary whose keys are the parameter names, and values are the annotation.

def foo(a,b):
    return(a+b)

def boo(a:'integer',b:'integer'=10)->'summation':
    '''
    function returns addition of two number 
    input:
        a (positional arg)
        b (default=10)
    output:
        a+b
    '''
    return(a+b)

def too(a:int,b:int)->int:
    '''
        sum of two numbers
    '''
    return(a+b)

# TODO: Factorial Implementation
# function helps to calculate factorial in recursive way
def fact(n: 'int >= 0')->int:
    '''Calculates n! (factorial function)
    
    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''
    
    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n-1)
    

if __name__=='__main__':
    help(print)
    help(foo)
    
    help(boo) #boo.__doc__
    print(boo.__annotations__)

    help(too)
    print(too.__annotations__)

    help(fact)
    print(fact.__annotations__)