'''markdown
| Tuple                                    |  List                                      |
|:----------------------------------------:|:------------------------------------------:|
| Sequence Types                           | Sequence Types                             |
| Immutable lists                          | Mutable Lists                              |
| Effecient unless you need mutability     | Useful in Mutablilty                       |
'''

from dis import dis 
from timeit import timeit
import sys

def fn(): pass 


# Tuple built up all at one time
print('Building (1,2,3,434565,"a")::')
dis(compile('(1,2,3,434565,"a")',filename='string',mode='eval'))

# List are built up one at a time
print('Building [1,2,3,434565,"a"]::')
dis(compile('[1,2,3,434565,"a"]',filename='string',mode='eval'))

# Addding mutability
print('Building includes mutability (fn,1,2,3,434565,"a")::')
dis(compile('(fn,1,2,3,434565,"a")',filename='string',mode='eval')) # No difference

# Addding mutability
print('Building [fn,1,2,3,434565,"a"]::')
dis(compile('[fn,1,2,3,434565,"a"]',filename='string',mode='eval'))


print("accessing (1,1.1,1.2,1.3,1.4):: {}".format(timeit("(1,1.1,1.2,1.3,1.4)",number=10_00_000)))
print("accessing [1,1.1,1.2,1.3,1.4]:: {}".format(timeit("[1,1.1,1.2,1.3,1.4]",number=10_00_000)))



# Copying List and Tuples
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

l2 = list(l1)    # l1, l2 are not same object
t2 = tuple(t1)   # t1, t2 are same object

print("L1::{} and L2::{} \nT1::{} and T2::{}".format(hex(id(l1)),hex(id(l2)),hex(id(t1)),hex(id(t2))))


# Storage Efficiency
# - In Mutable Object, the allocated capacity is greater than the number of elements (over-allocating)
# - In Immutable Object, are fixed when they have been created


print("{} TUPLE {}".format('-'*20,'-'*20))
# `NOTE`: As you can see the size delta for tuples as they get larger, remains a constant 8 bytes
prev = 0
for i in range(10):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1}\t items:{size_c},\t delta={delta}')



print("{} LIST {}".format('-'*20,'-'*20))
# `NOTE`: As you can see the size delta for LIST as they get larger, but delta changes
prev = 0
for i in range(10):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1}\t items:{size_c},\t delta={delta}')

# ![Dynamic Array](https://en.wikipedia.org/wiki/Dynamic_array)
    


t = tuple(range(100_000))
l = list(t)

# tuple directly access to pointers from element CPython
print("t=tuple(range(100000)) and accessing t[99989]= {}".format(timeit('t[99_989]', globals=globals(), number=10_000_000)))
#  List need to first access another array that contains the pointers to the element of the list
print("l=list(range(100000)) and accessing  l[99989]= {}".format(timeit('l[99_989]', globals=globals(), number=10_000_000)))