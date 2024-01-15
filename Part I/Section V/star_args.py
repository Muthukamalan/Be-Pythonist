# Unlike iterable unpacking, *args will be in tuples
# Once we use *args we can't use positional argument anymore. Only, Keyword arguments


def foo(a,b,*args,d):
    print(a)
    print(b)
    print(d)
    print(args,type(args))


if __name__=='__main__':
    try:
        foo(10,20,'a','b','c',100)
    except TypeError as te:
        print('not able to unpack properly!!')

    foo(102,103,'a','py','c++',d=323)

    # In this way, we can split our parameters into a required positional argument and rest