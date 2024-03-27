# Sequence Types
# An ordering of the sequence items using the natural numbers, starting index is set to 0.

## **Mutable Sequence Type**   - List, sets
## **Immutable Sequence Type** - String, Tuple, frozensets

from decimal import Decimal

numbers:tuple = (1,2,3)
print('index at 0️⃣th position ',numbers[0])

try:
    numbers[0]=10
except TypeError as te:
    print(te.__class__,'not mutable!')


mnumbers = ([1,10],2,3)
print('index at 0️⃣th position ',mnumbers[0])

mnumbers[0][-1] = 100
print("first element is a mutable object here: ",mnumbers)


# **Iterable**
# It is just something that can be iterated over. 

keystrokes:tuple = (10,'a',1+3j)
for keystorke in keystrokes: print(keystorke)

colors:set = {10,'a',1+3j}                        # set: not follow order
for col in colors: print(col)


# *in* and *not in* operator supports but not efficient
print('a' in keystrokes)

# len method to obtain number of items in the collection
print(f"number of keystrokes: {len(keystrokes)}")


# min,max  
# data types in the collection can be ordered
word:str = "The five boxing wizards jump quickly"
print(f'min:: `{min(word)}`')
print(f'max:: `{max(word)}`')


# Decimal('20.5')  -> constructor
# 20.5             -> literal
decimals:tuple = (10,20.5,Decimal('20.5')) 
print(f'min:: `{min(decimals)}`')
print(f'max:: `{max(decimals)}`')


# Concatenation
print(keystrokes+decimals)          # tuple
print([1,2,3,4]+[1+1j,2+1j,3+1j])   # list
print("hello"+" "+"world")          # string
print(''.join(tuple("hello") + (' ','w','o','r','l','d')))


# repetation
print('-'*10)
print(keystrokes*2)


# Indexing
#  These are basically searches that iterate over the sequence until they find (or not) the requested element.    
quote:str = "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program."
print("2nd occurance: {}".format(quote.index('o',2)))
try:
    print("2nd occurance: {}".format(quote.index('z')))
except ValueError as ve:
    print(ve.__class__,"not found!")



# Slicing
# It's ok to extend ranges past the bounds of the sequence:
print(quote[10:21])
print(keystrokes[1:5])
print(quote[20:9:-1])


# Immutable supports hashing
## sets are not hashable
## but frozensets are hashable.
print("quotes hash:: {}".format(hash(quote)))

colors = ('blue',['crimson','carmine','ruby'])
try:
    hash(colors)
except Exception as e:
    print(e.__class__)
