from collections import defaultdict

with open('0079_keylog.txt') as f:
    codes = f.read().splitlines()

order = defaultdict(set)

for a, b, c in codes:
    order[a].update({b, c})
    order[b].add(c)
    if not order[c]: order[c] = set()

passcode = list(order.keys())
passcode.sort(key=lambda d: len(order[d]), reverse=True)
print(''.join(passcode))