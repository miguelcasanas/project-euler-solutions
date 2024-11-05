from collections import deque

def gen():
    n, dq = 1, deque()
    while True:
        if not dq:
            dq.extend(str(n))
            n += 1
        yield int(dq.popleft())

indexes = [10**k for k in range(7)]

prod = 1
for i, d in enumerate(gen(), 1):
    if i in indexes: prod *= d
    if i == indexes[-1]: break

print(prod)