def is_pal(n, base):
    n = f"{n:{base}}"
    return n == n[::-1]

def is_double_pal(n):
    return is_pal(n, 'd') and is_pal(n, 'b')

print(sum(filter(is_double_pal, range(10**6))))