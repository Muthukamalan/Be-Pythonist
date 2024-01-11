'''
Python Type Hierarhy

                            # Numbers
                Integral                    Non-Integral
                    -int                        - floats
                    -boolean                    - complex
                                                - decimals
                                                - fractions

                        
                            # Collections
    Sequences                 Sets                       Mapping
mutable   immutable         mutable immutable       
-list       -tuples         -sets   -frozen sets        - dictionaries
            -strings

            
                            # Callable
                        - User Defined Functions
                        - Generators
                        - Classes
                        - Instance Methods
                        - Class Instances (__call__())
                        - Built-in Funcions (len,sum,open,..)
                        - Built-in methods 

                    
                            # Singletons
                        - None
                        - NotImplemented
                        - Ellipsis

'''

from typing import Callable
class Human:
        pass

if __name__=='__main__':
    
    print(type(1))
    print(type(True))

    print(type(1.0))
    print(type(1+3j))

    print(type([]))
    print(type((),))
    print(type(set()))
    print(type(frozenset()))

    print(type(''))
    print(type({}))

    
    h1 = Human()
    print(type(Human))
    print(type(h1))


    print(type(len))
    print(type(Callable))