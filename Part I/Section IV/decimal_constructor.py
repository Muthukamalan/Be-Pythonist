
import decimal
import sys
# Decimals have context, that can be used to specify rounding and precision (amongst other things)
# Decimals take up a lot more memory than floats.

# we can change setting in global context
# prec = 6, 28
# rounding = 'ROUND_HALF_EVEN' , 'ROUND_HALF_UP'

if __name__=='__main__':
    g_ctx = decimal.getcontext()
    print(g_ctx.prec)
    print(g_ctx.rounding)

    with decimal.localcontext()  as ctx:
        ctx.prec =10
        ctx.rounding = 'ROUND_HALF_UP'
        print(ctx.prec)
        print(ctx.rounding)

        # global prec
        print(g_ctx.prec)

    x = decimal.Decimal('1.234')
    print(x,type(x))

    a = 1.41414
    b = decimal.Decimal('1.41414')

    print(sys.getsizeof(a))
    print(sys.getsizeof(b))
