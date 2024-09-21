from sys import stdin
from collections import deque
from pprint import pprint


def bfs(sx, sy):
    global max_dist, res

    qu = deque([[sx, sy, 0]])
    visited[sx][sy] = 1
    start, end = 0, 0
    start = lst[sx][sy]

    while qu:
        x, y, cnt = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and lst[nx][ny]:
                visited[nx][ny] = cnt + 1
                qu.append([nx, ny, cnt + 1])

                end = lst[nx][ny]
                if cnt + 1 >= max_dist:
                    if cnt + 1 > max_dist:
                        res = start + end
                    elif cnt + 1 == max_dist:
                        res = max(res, start + end)
                    max_dist = cnt + 1


N, M = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0
max_dist = 0

for r in range(N):
    for c in range(M):
        if lst[r][c]:
            visited = [[0] * M for _ in range(N)]
            bfs(r, c)

print(res)
