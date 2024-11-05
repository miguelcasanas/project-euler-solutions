LIMIT = 10**6

divsum = [0] * (LIMIT + 1)

for n in range(1, LIMIT + 1):
    for m in range(2*n, LIMIT + 1, n):
        divsum[m] += n

def get_chain(origin):
    chain = [origin]
    while True:
        if (nxt := divsum[chain[-1]]) > 10**6: return []
        if nxt in chain:
            return chain if nxt == chain[0] else []
        chain.append(nxt)

longest_chain = max(map(get_chain, range(LIMIT + 1)), key=lambda x: len(x))
print(min(longest_chain))