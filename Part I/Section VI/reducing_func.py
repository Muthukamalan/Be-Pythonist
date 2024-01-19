# Reduce
# helps to come some aggregate 

from random import random
from functools import reduce

find_max = lambda x,y:x if x>y else y 
summation = lambda x,y:x+y      
product   = lambda x,y:x*y


numbers:list = list(sorted(range(1,50), key=lambda x:random()))

if __name__=='__main__':
    print(reduce(find_max,numbers))
    print(reduce(summation,numbers))          #sum(numbers)
    print(reduce(product,sorted(numbers)[:5]))