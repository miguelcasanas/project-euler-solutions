from more_itertools import last

def fib():
    a, b = 0, 1
    while True:
        yield a
        if len(str(a)) >= 1000: break
        a, b = b, a + b

print(last(enumerate(fib()))[0])