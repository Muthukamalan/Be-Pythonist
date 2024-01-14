
# Complex numbers are defined in rectangular coordinates (real and imaginary parts) using either the constructor or a literal expression.

import cmath

if __name__=='__main__':
    a = complex(1,2)
    print(a)

    print(a.real)
    print(a.imag)

    print(a.conjugate())
    print(cmath.sqrt(a))
