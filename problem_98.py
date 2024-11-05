from itertools import combinations, permutations
from collections import defaultdict
from string import digits
from math import sqrt
from re import findall

with open("0098_words.txt") as f:
    words = findall(r'\w+', f.read())

groups = defaultdict(list)
for word in words: groups[tuple(sorted(word))].append(word)

anagrams = []
for group in groups.values():
    if len(group) == 1: continue
    for comb in combinations(group, 2):
        anagrams.append(comb)

is_square = lambda n: sqrt(n).is_integer()

squares = set()
for pair in anagrams:
    letters = sorted(set(pair[0]))

    for perm in permutations(digits, l := len(letters)):
        mapping = {letters[i]: perm[i] for i in range(l)}
        numbers = [''.join(mapping[word[i]] for i in range(l)) for word in pair]
        
        if any(n[0] == '0' for n in numbers): continue

        numbers = set(map(int, numbers))
        if all(map(is_square, numbers)): squares |= numbers

print(max(squares))