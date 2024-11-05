def fib(limit):
    a, b = 0, 1
    while (c := a + b) <= limit:
        yield c
        a, b = b, c

is_even = lambda n: n % 2 == 0
print(sum(filter(is_even, fib(4_000_000))))