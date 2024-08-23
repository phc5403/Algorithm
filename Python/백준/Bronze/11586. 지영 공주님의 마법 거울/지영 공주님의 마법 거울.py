from sys import stdin
from pprint import pprint


def magic_mirror(num):
    if num == 2:
        for r in range(N):
            for c in range(N):
                res[r][c] = lst[r][N - 1 - c]

    elif num == 3:
        for r in range(N):
            for c in range(N):
                res[r][c] = lst[N - 1 - r][c]


N = int(stdin.readline())
lst = [list(stdin.readline().strip()) for _ in range(N)]
res = [[''] * N for _ in range(N)]
mind = int(stdin.readline())

if mind == 1:
    res = lst
else:
    magic_mirror(mind)

for row in range(N):
    for col in range(N):
        print(''.join(res[row][col]), end='')
    print()
