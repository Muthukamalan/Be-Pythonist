from time import perf_counter
from functools import wraps

 
def timed(fn,iters):
    # @wraps(fn)
    def inner(*args,**kwargs):
        total_elapsed = 0
        for _ in range(iters):
            start = perf_counter()
            res   = fn(*args,**kwargs)
            end   = perf_counter() 
            total_elapsed  += (end-start)
        avg_elapsed = total_elapsed / iters
        print('Avg run time: {0:.6f}s ({1} iterations)'.format(avg_elapsed,iters)) 
        return res 
    return inner


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)


def fib(n):
    return calc_fib_recurse(n)




'''
def subject(fn):
    print ("studying subject")
    def inner(*args, **kwargs):
        print("studing inner")
        return fn(*args, **kwargs)
    return inner

@subject                             # compiled in beginning..
def study_biology():
    print('studying biology!!')

# study_biology = subject(study_biology)
'''





def awake():
    print('am i still awake!!')
    def check_(fn):
        print('checking whaat')
        def inner(*args, **kwargs):
            print('running inner')
            return fn(*args, **kwargs)
        return inner
    return check_


@awake()                  # << check_ returns
def working_it():
    print('working in IT means ullala..')


doit = awake()             # awake returns decorator, so it's decorator factory

@doit                      # returned function works as decorator
def working_core():
    print('working in core means ullala!!')



if __name__=='__main__':
    N:int = 15
    # print("fib hex id:: {}".format(hex(id(fib))))
    fib = timed(fib,10)
    # print("fib hex id:: {}".format(hex(id(fib))))
    
    print(f"fibanocci of 15:: {fib(N)}")



    # study_biology()
    working_it()
    working_core()