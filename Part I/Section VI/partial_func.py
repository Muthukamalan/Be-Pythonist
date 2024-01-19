from functools import partial


def my_func(a, b, *args, k1, k2, **kwargs):
    print(f"a={a}, b={b}, args={args}, k1={k1}, k2={k2}, kwargs={kwargs}")

f2 = lambda a,b,*args,k1,**kwargs:my_func(a,10,args,k1=k1,k2=20,kwargs=kwargs)


# Sort complex number distance from origin
origin = 0+0j
ldisances =  [1+1j, 0+2j, -3+2j, 0+0j, 10+10j]
calcdistance = lambda x,y: (x.real-y.real )**2 + (x.imag-y.imag)**2


# 
def pow_(base,exponent):
    return pow(base=base,exp=exponent)

cube = partial(pow_,exponent=3)
squaree = partial(pow_,exponent=2)


if __name__=='__main__':
    f2(2,1,2,3,3,4,k1=100,k2=100,plot='kind')

    print(sorted(ldisances,key=lambda x: calcdistance(x,origin)))

    print(cube(9))