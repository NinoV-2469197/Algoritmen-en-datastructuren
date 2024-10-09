from plotter import count, lt, eq

def fib_it(n):
    a = 0
    b = 1
    c = 2
    for i in range(n):
        count()
        a = b
        b = c
        c = a + b
    return a

def fib_rec(n):
    if eq(n,0) or eq(n,1):
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)



def fib_dict_lookup(n):
    count()
    if n in dict:
        return dict[n]
    dict[n] = fib_dict_lookup(n-1) + fib_dict_lookup(n-2)
    return dict[n]

def fib_dict(n):
    global dict
    dict = {0: 0, 1: 1}
    return fib_dict_lookup(n)