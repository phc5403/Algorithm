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

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and lst[nx][ny] == '#':
                visited[nx][ny] = 1
                qu.append([nx, ny])


TC = int(stdin.readline())

for tc in range(1, TC + 1):
    R, C = map(int, stdin.readline().split())
    lst = [list(stdin.readline().strip()) for _ in range(R)]

    visited = [[0] * C for _ in range(R)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    res = 0

    for r in range(R):
        for c in range(C):
            if lst[r][c] == '#' and not visited[r][c]:
                bfs(r, c)
                res += 1

    print(res)