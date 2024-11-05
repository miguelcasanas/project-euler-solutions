from re import findall
from string import ascii_uppercase as letters

with open("0022_names.txt") as f:
    names = findall(r'\w+', f.read())
names.sort()

vals = {letters[i]: i + 1 for i in range(len(letters))}

alpha_value = lambda name: sum(vals[char] for char in name)
name_score = lambda i: (i + 1) * alpha_value(names[i])

print(sum(map(name_score, range(len(names)))))