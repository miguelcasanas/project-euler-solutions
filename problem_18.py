triangle = """TRIANGLE HERE"""

T = [
    list(map(int, row.split()))
    for row in triangle.splitlines()
]

def path_gen(i, j, path=[]):
    path = path + [T[i][j]]
    if i == len(T) - 1: yield path
    else:
        yield from path_gen(i + 1, j, path)
        yield from path_gen(i + 1, j + 1, path)

print(max(map(sum, path_gen(0, 0))))