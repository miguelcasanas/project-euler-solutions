from itertools import count, product
from string import ascii_lowercase as letters, printable
from operator import xor

with open("0059_cipher.txt") as f:
    cipher = list(map(int, f.read().split(',')))

allowed = set(printable[:94] + ' ')
words = ["the", "of", "is", "by", "to", "this"]

pass_gen = product(map(ord, letters), repeat=3)
for password in pass_gen:
    plain, rep = "", (password[i % 3] for i in count())
    for char in map(chr, map(xor, cipher, rep)):
        if char not in allowed: break
        plain += char
    else:
        if all(word in plain for word in words): break

print(sum(map(ord, plain)))