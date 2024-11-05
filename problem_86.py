from itertools import count, takewhile

squares = (n**2 for n in count(1))
squares = set(takewhile(lambda x: x < 2*10**8, squares))
is_square = lambda x: x in squares

def sols(M):
    total = 0
    for N in range(2, 2 * M + 1):
        if is_square(M**2 + N**2):
            total += M+1 - (N+1) // 2 if N > M+1 else N // 2
    return total

cum_total = 0
for M in count(1):
    cum_total += sols(M)
    if cum_total > 10**6: break

print(M)