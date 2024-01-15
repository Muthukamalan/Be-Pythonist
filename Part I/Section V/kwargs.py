# Positional parameters defined in functions can also be passed as named arguments.

def foo(a,b,c):
    print(f"a={a}, b={b}, c={c}")

def boo(*args,d):
    print(f"args={args}, d={d} ")


def too(*args,**kwargs):
    print(args)
    print(kwargs)

# Usual convention we follow
def yoo(a,*b,**kwargs):
    print(f"a={a}, b={b},  kwargs={kwargs}")



if __name__=='__main__':
    foo(a=10,c=30,b=20)  #keyword arguments

    boo(10,20,30,d=50)
    boo(d='bye')


    yoo(1,2,3,4,5,6,7,b=8,kwargs={'k1':"a",'k2':"b"})