l1 = [1,2,3,4]
l2 = [5,6]
print( hex(id(l1)), l1 )
print( hex(id(l2)), l2 )

l1=l1+l2
print("l1=l1+l2 \t l1::{} and l1={}".format( hex(id(l1)),l1) ) # new reference object

# Inplace Operation with `*=` / `+=`

l1 = [1,2,3,4]
l2 = [5,6]
print( hex(id(l1)), l1 )

l1+=l2
print("l1+=l2 \t l1::{} and l1={}".format( hex(id(l1)),l1) ) # same object `in-place concatenation`


l3 = 7,8
l1+=l3
print("l1+=l3 \t l1::{} and l1={}".format( hex(id(l1)),l1) )

l4 = {11,12,13}
l1+=l4 
print("l1+=l4 \t l1::{} and l1={}".format( hex(id(l1)),l1) )
