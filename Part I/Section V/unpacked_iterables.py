# Unpacking Iterables
# Unpacking is a way to split an iterable object into individual variables contained in a list or tuple

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

x,y,*other,z = list_of_numbers
# *\** operator can only appear **once**!

if __name__=='__main__':
    a:tuple = 1,
    print(type(a))

    b = (2)
    print(type(b))

    c = (1,)
    print(type(c))


    # Swap two numbers
    a,b = b,a 
    print(f"a={a}, b={b}")


    print(x,y,z)
    print(''.join( str(i) for i in other))


    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    s3 = {5, 6, 7}
    s4 = {7, 8, 9}
    print(s1.union(s2).union(s3).union(s4))
    # print(s1.union(s2, s3, s4))


    print({*s1,*s2,*s3,*s4})


    # Nested Unpacking
    a, b, (c, d,*e) = [1, 2, 'python']
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)