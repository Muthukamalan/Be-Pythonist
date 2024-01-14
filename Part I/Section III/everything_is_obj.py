# In python, everything is object

# Any object can be assigned to variable include fucntions, function can return function as well.

# Functions are 1st class citizens
from math import sqrt
if __name__=="__main__":
    a = int('1010111',base=2)
    print(a,type(a))

    f= sqrt
    print(f,type(f))