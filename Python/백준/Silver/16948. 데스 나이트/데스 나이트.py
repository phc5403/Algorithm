from sys import stdin
from collections import deque


def bfs(sx, sy):
    global res
    qu = deque([[sx, sy, 0]])
    visited[sx][sy] = 1

    while qu:
        x, y, cnt = qu.popleft()

        if res != float("inf") and res >= cnt:
            continue

        if [x, y] == [r2, c2]:
            res = min(res, cnt)
            break

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                qu.append([nx, ny, cnt + 1])


N = int(stdin.readline())
r1, c1, r2, c2 = map(int, stdin.readline().split())

# (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)
# 상상좌, 상상우, 좌좌, 우우, 하하좌, 하하우
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

visited = [[0] * N for _ in range(N)]
res = float("inf")

bfs(r1, c1)

if res != float("inf"):
    print(res)
else:
    print(-1)