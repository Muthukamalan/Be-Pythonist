from inspect import isfunction,ismethod,getcomments,cleandoc,signature,getmodule

# TODO: Factorial Implementation (Recursion)
def fact(n: 'some non-negative integer',default:int=1) -> 'n! or 0 if n < 0':
    """Calculates the factorial of a non-negative integer n
    
    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
fact.short_description = 'factorial function'


def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    i=0
    pass




class Human:
    __slots__ = '_height','_weight'                            # deny monkey patching
    def __init__(self,height:int,weight:int) -> None:
        self._height:int = height
        self._weight:int  = weight

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,new_val):
        self._height = new_val


    @staticmethod
    def f_static():
        pass

    def __str__(self) -> str:
        return(f"human of height={self.height} and weight={self._weight}")


def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')
    print(f"module name= {getmodule(f)}\n")
    print('{0}\n{1}\n'.format(getcomments(f), 
                              cleandoc(f.__doc__)))
    
    print('{0}\n{1}'.format('Inputs', '-'*len('Inputs')))
    
    sig = signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')
        
    print('{0}\n{1}'.format('\n\nOutput', '-'*len('Output')))
    print(sig.return_annotation)


if __name__=='__main__':
    print(fact.short_description)
    print(fact.__doc__)
    print(fact.__annotations__)
    print(fact.__name__)
    print(fact.__defaults__)
    print(fact.__code__)  # << callable

    print(my_func.__kwdefaults__)
    print(my_func.__code__.co_varnames)

    my_func_code = my_func.__code__ 
    for method in [i for i in dir(my_func_code) if not i.startswith('_')]:
        print(method," ", getattr(my_func_code,method))


    x = Human(23,41)
    print(x._height)
    print(dir(x))

    print_info(fact)