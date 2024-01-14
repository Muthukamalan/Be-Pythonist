# variable_name : type = value; 

# Python is dynamically typed.
# This means that the type of a variable is simply the type of the object the variable name points to (references). The variable itself has no associated type.

from typing import Any
if __name__=='__main__':
    a:int = 10 
    print(type(a))

    a:Any = lambda x:x**2
    print(type(a))