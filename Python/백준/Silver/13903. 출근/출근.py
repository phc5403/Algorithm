from sys import stdin
from collections import deque


def bfs():
    global res

    qu = deque()
    visited = [[False] * M for _ in range(N)]

    for col in range(M):
        if lst[0][col]:
            qu.append([0, col, 0])
            visited[0][col] = True

    while qu:
        x, y, cnt = qu.popleft()

        if x == N - 1:
            return cnt

        for k in range(K):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and lst[nx][ny]:
                visited[nx][ny] = True
                qu.append([nx, ny, cnt + 1])

    return -1


N, M = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]
K = int(stdin.readline())

dx, dy = [], []
res = float('inf')

for _ in range(K):
    kx, ky = map(int, stdin.readline().split())

    dx.append(kx)
    dy.append(ky)

res = bfs()
print(res)