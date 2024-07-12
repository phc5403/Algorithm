from sys import stdin
from collections import deque
from pprint import pprint


def bfs(r, c):
    cnt = 1
    qu = deque()
    qu.append([r, c])

    while qu:
        x, y = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny]:
                cnt += 1
                lst[nx][ny] = 0
                qu.append([nx, ny])

    return cnt


N, M = map(int, stdin.readline().split())

lst = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []

for row in range(N):
    for col in range(M):
        if lst[row][col]:
            lst[row][col] = 0
            res.append(bfs(row, col))

print(len(res))
if res:
    print(max(res))
else:
    print(0)
