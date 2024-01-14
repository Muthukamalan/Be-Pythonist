
from typing import Any
from variable_memoryref import memory_check
from ref_count import ref_count
import gc

def process(s):
    print(f"s:= {hex(id(s))}"); 
    ref_count((id(s)))
    s = s+'hello'
    print(f"s:= {hex(id(s))}")
    return s


if __name__=='__main__':
    a = 'Muthu'
    print(f"a:= {hex(id(a))}")  

    a = process(a)
    print(f"a:= {hex(id(a))}") 