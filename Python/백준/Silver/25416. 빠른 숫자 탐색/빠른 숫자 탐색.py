from sys import stdin
from collections import deque


def bfs(sx, sy):
    global res

    qu = deque([[sx, sy, 0]])
    visited[sx][sy] = 1

    while qu:
        x, y, cnt = qu.popleft()

        if lst[x][y]:
            res = min(res, cnt)
            return

        if res < cnt:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and not lst[nx][ny] == -1:
                visited[nx][ny] = 1
                qu.append([nx, ny, cnt + 1])


lst = [list(map(int, stdin.readline().split())) for _ in range(5)]
sx, sy = map(int, stdin.readline().split())

visited = [[0] * 5 for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = float('inf')

bfs(sx, sy)


if res != float('inf'):
    print(res)
else:
    print(-1)