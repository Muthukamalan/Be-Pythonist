# A list comprehension is language construct that allows to easily build a list by transforming, and optionally, filtering, another iterable.

import dis
from math import factorial

squares = [i**2 for i in range(1, 51)]
print(squares[:10])


compiled_code = compile('[i**2 for i in (1, 2, 3)]', filename='', mode='eval')
dis.dis(compiled_code)


table = [ [i * j for j in range(1, 11)] for i in range(1, 11)]

# C(n,k) = n! / (k! (n-k)!)
def combinations(n,k):
    return factorial(n) // (factorial(k)*factorial(n-k))


size = 10
pascal = [[combinations(n,k) for k in range(n+1)] for n in range(size+1) ]



l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

results = [ i+j for j in l2 for i in l1 if i!=j]



# Each Scopes are seperate
funcs = [lambda x: x**0, lambda x: x**1, lambda x: x**2, lambda x: x**3]
print("[lambda x: x**0, lambda x: x**1, lambda x: x**2, lambda x: x**3]:: ")
print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10))

#  BUT ?? What's happening?
funcs = []
for i in range(4):
    funcs.append(lambda x:x**i)
print("In For Loop,")
print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10))


# Even in List Comphrension also???
funcs = [ lambda x:x**i for i in range(4)]
print("[ lambda x:x**i for i in range(4)]::")
print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10))


# Resolve!!
funcs = [ lambda x,pow=i:x**pow for i in range(4)]
print("[ lambda x,pow=i:x**pow for i in range(4)]::")
print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10))

# default values are evaluated and stored with the function's definition **when the function is being created (i.e. compiled)**. Right now we are running into a problem because the free variable `i` is being evauated inside each function's body at **run time**.