from sys import stdin
from collections import deque


def bfs(sx, sy):
    global sheep, wolf

    qu = deque([[sx, sy]])
    visited[sx][sy] = 1
    sh, wo = 0, 0

    while qu:
        x, y = qu.popleft()

        if lst[x][y] == 'v':
            wo += 1
        elif lst[x][y] == 'k':
            sh += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and lst[nx][ny] != '#':
                visited[nx][ny] = 1
                qu.append([nx, ny])

    if sh > wo:
        wolf -= wo
    else:
        sheep -= sh


R, C = map(int, stdin.readline().split())

lst = [list(stdin.readline().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

sheep, wolf = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for r in range(R):
    for c in range(C):
        if lst[r][c] == 'v':
            wolf += 1
        elif lst[r][c] == 'k':
            sheep += 1

for r in range(R):
    for c in range(C):
        if lst[r][c] != '#' and not visited[r][c]:
            bfs(r, c)

print(sheep, wolf)