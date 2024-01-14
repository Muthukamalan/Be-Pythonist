from typing import AnyStr

# The term  shared ref is the concept of two variables referencing the **same** object in memory

if __name__=='__main__':

    # Shared Reference
    a = 'greet'
    b = a 
    print(f"{hex(id(a))} == {hex(id(b))} :: {hex(id(a))==hex(id(b))}")

    # Immutable
    a = 10;
    b = 18-8;
    print(f"{hex(id(a))} == {hex(id(b))} :: {hex(id(a))==hex(id(b))}")

    # Shared Reference
    l1 = [1,2,3,4]
    l2 = l1 
    print(f"{hex(id(l1))} == {hex(id(l2))} :: {hex(id(l1))==hex(id(l2))}")

    # Mutable
    l1 = [1,2,3]
    l2 = [1,2,3]
    print(f"{hex(id(l1))} == {hex(id(l2))} :: {hex(id(l1))==hex(id(l2))}")