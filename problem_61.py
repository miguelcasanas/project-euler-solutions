from itertools import count, chain
from collections import defaultdict

numbers = defaultdict(list)
for k in range(3, 9):
    for n in count():
        if (x := n*((k - 2)*n - k + 4) // 2) >= 10**4: break
        if x > 10**3: numbers[k].append((k, str(x)))

paths = [[x] for x in numbers[8]]
for _ in range(5):
    new_paths = []
    for path in paths:
        for k, x in chain(*numbers.values()):
            K = set(node[0] for node in path)
            if k in K: continue
            if x[:2] == path[-1][1][2:]:
                new_paths.append(path + [(k, x)])
    paths = new_paths

paths = [p for p in paths if p[-1][1][2:] == p[0][1][:2]]
result = sum(int(node[1]) for node in paths[0])
print(result)