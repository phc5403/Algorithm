from sys import stdin
from collections import deque
from pprint import pprint


def bfs(sx, sy):
    global res

    qu = deque()
    qu.append([sx, sy])
    cnt = 1

    while qu:
        x, y = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and lst[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                qu.append([nx, ny])

    return cnt


N, M, K = map(int, stdin.readline().split())

lst = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for _ in range(K):
    a, b = map(int, stdin.readline().split())
    lst[a - 1][b - 1] = 1

# pprint(lst, width=40)
# pprint(visited, width=60)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
res = float('-inf')

for r in range(N):
    for c in range(M):
        if lst[r][c]:
            visited[r][c] = True
            res = max(res, bfs(r, c))

print(res)