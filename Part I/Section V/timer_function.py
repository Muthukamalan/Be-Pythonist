import time

def time_it(fn, *args, rep=5, **kwargs)->None:
    start = time.perf_counter()
    for i in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()
    time_taken = end - start
    time_taken_per_loop = time_taken/rep 
    print(f"time taken for fn{time_taken} for each rep {time_taken_per_loop}")
    

def compute_power_3(n,*,start=1,end):
    return [n**i for  i in range(start,end)]

def compute_power_set3(n,*,start=1,end):
    return (n**i for  i in range(start,end))


# Closures
# We want our function to cache results, so that we don't recalculate something more than once.
# n! = n*(n-1)!

def factorial(n):
    if n<1:
        return 1
    else:
        print(f'calcuating {n}!')
        return n*factorial(n-1)
    

def smart_factorial(n,cache={}):
    if n<1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f'calcuating {n}!')
        result = n*smart_factorial(n-1)
        # print(f'cached:: {cache}')
        cache[n] = result
        return result 




if __name__=='__main__':
    # time_it( compute_power_set3,n=2,end=20000,rep=3 )
    # time_it( compute_power_3,n=2,end=20000,rep=3   )

    
    # print(factorial(7))
    # print(smart_factorial(7))

    # time_it(smart_factorial,n=17,rep=10)
    # time_it(factorial,n=17,rep=10)

    pass