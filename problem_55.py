def is_palindromic(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if is_palindromic(n): return False
    return True

print(sum(map(is_lychrel, range(10_000))))