# [garbage reference]('./assets/circular_ref.png')

import ctypes
import gc 

from ref_count import ref_count
from variable_memoryref import memory_check

def object_by_id(obj_id):
    for obj in gc.get_objects():
        if id(obj)==obj_id:
            return("object exists")
    return('not found')
    


# Circular Reference
class A:
    def __init__(self) -> None:
        self.b = B(self)
        print(f'calling init in class A!! A:self={hex(id(self))},\tB:{hex(id(self.b))}')

class B:
    def __init__(self,a) -> None:
        self.a = a
        print(f'calling init in class B!! B:self={hex(id(self))},\tA:{hex(id(self.a))}')


def boo(my_var):
    print('a: \t{0}'.format(hex(id(my_var))))
    print('a.b: \t{0}'.format(hex(id(my_var.b))))
    print('b.a: \t{0}'.format(hex(id(my_var.b.a))))

if __name__=='__main__':
    # Disabling Garbage Collection
    gc.disable()
    a = A()
    memory_check(a)
    ref_count(id(a))
    boo(a)
    print('-'*50)
    
    a_id = id(a); 
    ref_count(a_id)
    print(f"{hex(a_id)} and it's {object_by_id(a_id)}")

    b_id = id(a.b); 
    ref_count(b_id)
    print(f"{hex(b_id)} and it's {object_by_id(b_id)}")
    print('*'*50)
    
    # MAKING VARIABLE AS NONE
    a = None
    ref_count(a_id)
    print(f"{hex(a_id)} and it's {object_by_id(a_id)}")

    ref_count(b_id)
    print(f"{hex(b_id)} and it's {object_by_id(b_id)}")
    print('*'*50)

    # Run Garbage Collection
    gc.collect()
    ref_count(a_id)
    print(f"{hex(a_id)} and it's {object_by_id(a_id)}")

    ref_count(b_id)
    print(f"{hex(b_id)} and it's {object_by_id(b_id)}")

