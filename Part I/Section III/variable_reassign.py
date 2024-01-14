from typing import Any,SupportsInt
from variable_memoryref import memory_check

if __name__=='__main__':
    a:int = 10 
    print(f"a:={hex(id(a))}")
    # memory_check(a)

    # Re-Assign
    a: int = 15
    print(f"a:={hex(id(a))}")   # << different memory address

    # Modify Element 
    a += 1
    print(f"a:={hex(id(a))}")


    # New instance 
    b:int = 16
    print(f"b:={hex(id(b))}")

    # The memory addresses of both **a** and **b** are the same!! 