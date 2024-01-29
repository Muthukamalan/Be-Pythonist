# Object of type ModuleType

# How Python imports a module from file:
#   - checks the sys.modules cache to see if the module has already been imported.
#   - creates a new module object
#   - loads the source code from file
#   - adds an entry to sys.modules with name as key and the newly create
#   - compiles and executes the source code     

import modlol
import fractions
import math
import sys
from types import ModuleType
from collections import namedtuple

print(modlol)
print(modlol.crazyword('crazy word','Muthu'))
del globals()['modlol']


def foo():
    pass 


mod = ModuleType('test','This is test modules')
mod.pi = 3.14;
mod.hello = lambda x:print(f"Hello, {x}")
mod.Point = namedtuple('Point','x y z')


# Reloading Modules won't impact untill unless detach ref and attach again.
# import importlib
# importlib.reload('module_name')
# from math import sqrt
# math in globals() # False
# importlib.reload(sys.modules['math])

if __name__=='__main__':
    print(foo,type(foo),hex(id(foo)))

    for i in list(globals()):
        print(f"{i}::::{globals().get(i,None)}")

    print(fractions) #'C:\\Users\\muthu\\miniconda3\\envs\\ojenv\\lib\\fractions.py'
    print(math)      # build-in ?


    # for k,v in sys.modules.items():
    #     print(f"{k}:::::{v}")

    print(math.__dict__,end='\n')


    print(isinstance(fractions,ModuleType))
    print(isinstance(math,ModuleType))
    print(isinstance(mod,ModuleType))
    print(mod.__dict__)
    mod.hello("world!")
    p1 = mod.Point(1,2,3)
    p2 = mod.Point(1,2,3)

    print(p1==p2)


    # where python installed?
    print(sys.prefix)
    print(sys.exec_prefix)  # executable c binaries located


    # where does python look for imports
    print(f"number of path look for {len(sys.path)}")
    print(sys.path)


    # python -m zipfile - filename.zip . 
    #  -m module 
    #  -c create
    # python -m zipfile -l file_name.zip