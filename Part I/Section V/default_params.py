
def foo(a,b,c):
    '''Positional Arguments'''
    print("a={0}, b={1}, c={2}".format(a,b,c))

def boo(a,b=10,c=20):
    '''Default values, once thy assigned all parameters assigned therafter'''
    print("a={0}, b={1}, c={2}".format(a,b,c))

# Keyword Arguments (named arguments)
# can be optionally , this allo us to pass arguments without using positional assignment


if __name__=='__main__':
    
    foo(5,10,20)

    boo(50,c=32,b=3)