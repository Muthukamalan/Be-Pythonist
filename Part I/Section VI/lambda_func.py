import string
from random import random


# Lambda function
# helps to create anonymous functions (without function name) and returns (inline condition)

# first-class functions
#   - we can directly assign to variable.

squre = lambda x:x**2

add_but_ten_as_default = lambda x,y=10:(x+y)

func1 = lambda x,y=2,*args,kw1,kw2=10,**kwargs:("x={0}, y={1}, args={2}, kw1={3}, kw2={4} and kwargs={5}".format(x,y,args,kw1,kw2,kwargs))

# Higher Order Functions
# accepts function and return another function or value
def new_func(a,fn):
    return(fn(a))


def func2(fn,*args,**kwargs):
    return fn(*args,**kwargs)



# SORT
shuffled_letters:list =  sorted(list(string.ascii_letters),key=lambda _:random(),reverse=True)

sorted_letters_without_key:list   = sorted(shuffled_letters)
sorted_letters_with_key:list      = sorted(shuffled_letters,key=ord,reverse=True)  #key=str.upper  #key=str.lower

marks:list = {'tamil': 94, 'english': 83, 'math': 95, 'science':78, 'social':90}


if __name__=='__main__':

    print(f"type of square::{type(squre)} and it's name::{squre.__name__}")
    print("square of 4= {}".format(squre(4)))

    print("add_10 to numbe 4r= {}".format(add_but_ten_as_default(4)))
    print("add_10 to number but pass 2 int= {}".format(add_but_ten_as_default(4,1)))

    print(func1(2,4,6,8,10,kw1=100,print='false',kind='true'))

    print(f"square of 5 = {new_func(5,squre)}")  # square = lambda x:x**2

    print(func2(func1,2,4,6,8,10,kw1=100,print='false',kind='true'))


    print(shuffled_letters)
    print(sorted_letters_without_key)
    print(sorted_letters_with_key)

    print(sorted(marks,key=lambda x:marks[x]))


    # challenge
    solution = ''.join(sorted('abcdefg', key = lambda x: random()))
    print(solution)