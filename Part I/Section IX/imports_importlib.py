# Finder
# Loader
# Finder + Loader = import


import sys
import collections
import importlib
import os

mod_name = 'math'
try:
    import mod_name 
except Exception as e:
    print(e.__repr__())



mat = importlib.import_module(mod_name)
print('math' in sys.modules)
print('mat' in globals())
print(mat.sin(20))
# print(dir(mat))





if __name__=='__main__':
    print(sys)
    # Finder Objects
    print('\n\n----------------')
    for i in sys.meta_path: print(i)
    print('----------------\n\n')

    print(collections)
    print(collections.__spec__)
    

    for k,v in os.environ.items():
        print(f"{k}::\t{v}")

    