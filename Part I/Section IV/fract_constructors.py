from fractions import Fraction

if __name__=='__main__':
    print(help(Fraction))

    f1 = Fraction(1)
    print(f1)

    f2 = Fraction(1,3)
    print(f2)

    x = Fraction(2,3)
    y = Fraction(3,4)
    print(Fraction(x,y))


    f3 = Fraction(.125)
    print(f3)

    f4 = Fraction('22/7')
    print(f4)
    
    f5 = Fraction(1,-4)
    print(f5)
    print(f5.numerator)
    print(f5.denominator)

    
