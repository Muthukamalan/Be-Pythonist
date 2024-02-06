# Object
# - contains data -> state
# - contains functionality -> behavior

# Class is like a template used to create objects


class MyClass(object):
    pass 


if __name__=='__main__':
    print(MyClass)
    # print(dir(MyClass))
    print(MyClass.__name__)

    p = MyClass()
    print(type(p), p.__class__)

    # meta programming
    print(type(type),type(str),type(MyClass))