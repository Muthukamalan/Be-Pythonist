
if __name__=='__main__':

    # Shared Reference
    a = 'greet'
    b = a 
    print(f"{hex(id(a))} == {hex(id(b))} :: {hex(id(a))==hex(id(b))}")           # << CONTENT are same
    print(f"{hex(id(a))} is {hex(id(b))} :: {hex(id(a)) is hex(id(b))}")         # is Same Object ??      # CHECKS MEMORy


    # Immutable
    a = 10;
    b = 18-8;
    print(f"{hex(id(a))} == {hex(id(b))} :: {hex(id(a))==hex(id(b))}")
    print(f"{hex(id(a))} is {hex(id(b))} :: {hex(id(a)) is hex(id(b))}")         # is Same Object ?


    a = 10;
    b = 10.0;
    print(f"{a}:{hex(id(a))} == {b}:{hex(id(b))} :: {hex(id(a))==hex(id(b))}")
    print(f"{hex(id(a))} is {hex(id(b))} :: {hex(id(a)) is hex(id(b))}")





    # Shared Reference
    l1 = [1,2,3,4]
    l2 = l1 
    print(f"{hex(id(l1))} == {hex(id(l2))} :: {hex(id(l1))==hex(id(l2))}")

    # Mutable
    l1 = [1,2,3]
    l2 = [1,2,3]
    print(f"{hex(id(l1))} == {hex(id(l2))} :: {hex(id(l1))==hex(id(l2))}")


    # NoneType

    a = None
    b = None 
    print(f"{a} is {b} :: {a is b}")
    print(f"{a} == {b} :: {a == b}")

    l = []
    print(f"{a} == {l} :: {a == l}")
    print(f"{a} is {l} :: {a is l}")
