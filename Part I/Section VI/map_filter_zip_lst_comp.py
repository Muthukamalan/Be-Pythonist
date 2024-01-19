# Higher-Order-Functions: Map and Filter
# Takes function as argument and returns function/value



import string
from random import random

shuffled_letters:list =  sorted(list(string.ascii_letters),key=lambda _:random(),reverse=True)


def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

power:int = lambda x,y: x**y

truthy:list = [0,'abc',1,{},34, 4+5j, None, (2,4,None)]


l1 = [1,2,3,4]
l2 = 'python'
l3 = 10,20,30,40

if __name__=='__main__':
    print(factorial(5))
    print(list(map(factorial,range(1,5+1))))
    print(list(map(power,(3,4),(0,5) )))
    # help(map)                                      # returns non-exhastive sequence
    
    # help(filter)                                   # returns filtered contents
    print(list(filter(None,truthy)))
    print(list(filter(lambda x:x%2==0, range(50,100))))

    # List Comprehension and zip
    # help(zip)
    print([(i,i**2) for i in range(50,100) if i%2==0])
    print({j:i+k  for i,j,k in zip(l1,l2,l3)})