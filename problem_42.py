from re import findall
from string import ascii_uppercase as letters

with open("0042_words.txt") as f:
    words = findall(r'\w+', f.read())

values = {letters[i]: i + 1 for i in range(len(letters))}

def get_value(name):
    return sum(values[char] for char in name)

T = {n * (n + 1) // 2 for n in range(100)}

result = sum(1 for w in words if get_value(w) in T)
print(result)