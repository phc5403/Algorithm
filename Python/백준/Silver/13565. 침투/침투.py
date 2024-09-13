from sys import stdin
from collections import deque
from pprint import pprint


def bfs(sx, sy):
    global res

    qu = deque([[sx, sy]])
    # visited = [[False] * M for _ in range(N)]

    while qu:
        x, y = qu.popleft()

        if x == 0:
            res = "YES"
            return

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not lst[nx][ny]:
                visited[nx][ny] = True
                qu.append([nx, ny])


N, M = map(int, stdin.readline().split())

lst = [list(map(int, stdin.readline().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = "NO"

for m in range(M):
    if not lst[N-1][m]:
        bfs(N-1, m)

print(res)