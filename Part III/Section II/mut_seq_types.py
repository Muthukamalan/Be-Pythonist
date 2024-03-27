# Mutable Sequence Types


numbers = [1,2,3,4,5]
print(numbers,hex(id(numbers)))  #Original

numbers.clear()
print(numbers,hex(id(numbers)))  
# reference not changed.  The sequence's memory address has not changed, but the internal state of the sequence has.


numbers = [1,2,3,4,5]
print(numbers,id(numbers))  #Original
numbers = []
print(numbers,id(numbers))  # Results could be same. Memory Changed.



colors:list = ['crimson','ruby','brick','scarlet','maroon']
reds:list   = colors   # Copied to another ref variable
colors.clear()         # 
print("{} in {} and {} in {}".format(colors,hex(id(colors)), reds, hex(id(reds)) ) )  # Both Affected


colors:list = ['crimson','ruby','brick','scarlet','maroon']
reds:list   = colors   # Copied to another ref variable
colors      = []
print("{} in {} and {} in {}".format(colors,hex(id(colors)), reds, hex(id(reds)) ) )  # Not Affected


# Slicing do operations on same ref
colors:list = ['crimson','ruby','brick','scarlet','maroon']
print("{0:120s} {1}".format("{}".format(colors), hex(id(colors))))
colors[0:2] = ['raspberry','coral','redwood']
print("{0:120s} {1}".format("{}".format(colors), hex(id(colors))))


# Append do operation on same ref
colors.append('raspberry')
print("{0:120s} {1}".format("{}".format(colors), hex(id(colors))))
# Same for Extend
colors.extend(['raspberry','coral','redwood'])
print("{0:120s} {1}".format("{}".format(colors), hex(id(colors))))
# Same for Pop
colors.pop()
print("{0:120s} {1}".format("{}".format(colors), hex(id(colors))))
# Same for Reverse
colors.reverse()
print("{0:120s} {1}".format("{}".format(colors), hex(id(colors))))


# Returns New Object
print("{0:120s} {1}".format("{}".format(colors[::-1]), hex(id(colors[::-1]))))