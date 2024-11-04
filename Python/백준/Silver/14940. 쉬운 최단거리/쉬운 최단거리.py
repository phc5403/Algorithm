from sys import stdin
from collections import deque
from pprint import pprint


def bfs(sx, sy):
    qu = deque([[sx, sy]])
    visited[sx][sy] = 1

    while qu:
        x, y = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and lst[nx][ny]:
                visited[nx][ny] = 1
                lst[nx][ny] = lst[x][y] + 1
                qu.append([nx, ny])


def find_start():
    for n in range(N):
        for m in range(M):
            if lst[n][m] == 2:
                lst[n][m] = 0
                return bfs(n, m)


N, M = map(int, stdin.readline().split())

lst = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

find_start()

for r in range(N):
    for c in range(M):
        if lst[r][c] == 1 and not visited[r][c]:
            lst[r][c] = -1

for row in lst:
    print(*row)

# pprint(lst, width=80)