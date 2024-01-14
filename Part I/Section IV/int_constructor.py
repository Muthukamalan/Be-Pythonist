
# Boolean      False or True

# Integer Number (Z)  :: -n,-(n-1),...0,1,2,....n
# Ration Number  (Q)  :: {p}\over{q}
# Real Number    (R)  :: 0,-1,0.32323, 1/3, np.pi
# Complex Number (C)  :: a+bj

# Z ⊆ Q ⊆ R ⊆ C
 
# If we want to use `n` bits to store integer, our range would be::
# [ 2^(n-1)-1, 2^(n-1) ]



#  / returns float
#  % modulo operator


import sys
if __name__=='__main__':
    a = 100;
    print(type(a))


    print(sys.getsizeof(0))
    print(sys.getsizeof(10000000000))
    print(sys.getsizeof(0.323))


    a = -13
    b = -4
    print('{0}**{1} = {2}'.format(a, b, a**b))
    print('{0}+{1} = {2}'.format(a, b, a+b))
    print('{0}/{1} = {2}'.format(a, b, a/b))
    print('{0}//{1} = {2}'.format(a, b, a//b))
    print('{0}%{1} = {2}'.format(a, b, a%b))
    print(a == b * (a//b) + a%b)
    

    a = int(10)
    print(a)


    a = int(10.9)
    print(a)      # truncated 

    a = int(-10.9)
    print(a)      # truncated 


    a = int(True)
    print(a)

    a = int("10")
    print(a)

    a = int('10101010111',base=2)
    print(a)

    a = int('10101010A111',base=16)
    print(a)

    binary_a = bin(a)
    print(binary_a,type(binary_a))

    
    oct_a = oct(a)
    print(oct_a,type(oct_a))
    
    hex_a = bin(a)
    print(hex_a,type(hex_a))