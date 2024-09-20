from sys import stdin
from collections import deque


def bfs(sx, sy):
    qu = deque()
    qu.append([sx, sy])
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True

    while qu:
        x, y = qu.popleft()

        for k in range(7):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and lst[nx][ny] == '.':
                res.append([nx, ny])
                visited[nx][ny] = True
                qu.append([nx, ny])

    return False


N = int(stdin.readline())
lst = [list(stdin.readline().strip()) for _ in range(N)]

# dx = [-1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 1, -1, 1, 1, 0, -1]

# 목적지부터 역으로 탐색하므로, 기존 7방향을 반대로 변경.
dx = [1, 1, 0, 0, -1, -1, -1]
dy = [1, -1, 1, -1, -1, 0, 1]

res = []

for r in range(N):
    for c in range(N):
        if lst[r][c] == 'F':
            bfs(r, c)
            break

print(len(res))
