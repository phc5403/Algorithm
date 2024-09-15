from sys import stdin

N, M = map(int, stdin.readline().split())
lst = [list(stdin.readline().strip()) for _ in range(N)]

for row in range(N):
    for col in range(M):
        if lst[row][col] != '.':
            lst[row][M - col - 1] = lst[row][col]

for r in range(N):
    for c in range(M):
        print(lst[r][c], end='')
    print()