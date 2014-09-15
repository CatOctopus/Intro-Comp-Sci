def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def switch(x,y):
    z=x
    x=y
    y=z
    return(x,y)

def areatri(b,h):
    return b*h*.5

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
