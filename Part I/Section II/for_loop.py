# In py, any iterable object, capable of returning values one at a time.

# *for* keyword can be used to iterate and iterable.

'''py

i:int = 0 
while i<5:
    print(i) # execute block
    i += 1
i = None

for i in range(5):
    print(i)  # execute block
'''

from typing import Optional,Union
def iterables(iterable:Optional[Union[list,str,tuple,set]])->None:
    for i in iterable:
        print(i)
    print('*'*50)

if __name__=='__main__':
    iter1 = list((1,2,3,4,5))  # << list
    iterables(iter1)

    iter2 = range(100,105)     # << range
    iterables(iter2)
    
    iter3 = tuple((1,2,3,4))   # << tuple
    iterables(iter3)
    
    iter4 = [
        [1,2,3],
        [4,5,6]
    ]
    iterables(iter4)           # << list of list //ndarray 
    
    iter5 = 'muthu'
    iterables(iter5)           # << str

    iter6 = set((4,5,6,7))
    iterables(iter6)           # << set

    # enumerate
    for idx,val in enumerate(iter1):
        if idx==0:
            print('idx','val')
        print(idx,val)