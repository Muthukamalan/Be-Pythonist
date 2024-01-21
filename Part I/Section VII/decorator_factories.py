from time import perf_counter


def timed_factory(num_iters=10):
    def timed(fn):
        def inner(*args,**kwargs):
            total_elapsed = 0
            for _ in range(num_iters):
                start = perf_counter()
                res   = fn(*args,**kwargs)
                end   = perf_counter()
                total_elapsed += (end-start)
            avg = total_elapsed/num_iters
            print('Avg run time: {0:.2f}s {1} iterations'.format(avg,num_iters))
            return res 
        return inner
    return timed


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)

@timed_factory(30)
def fib(n):
    return calc_fib_recurse(n)
# print(timed_factory(30)(fib)(30))


if __name__=='__main__':
    print(fib(30))