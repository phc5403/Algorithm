from sys import stdin
from collections import deque


def bfs():
    global res

    qu = deque([[0, 0, 0]])
    visited[0][0] = True

    while qu:
        x, y, cnt = qu.popleft()

        if cnt > res:
            continue

        if [x, y] == [X, Y]:
            res = min(res, cnt)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if -500 <= nx <= 500 and -500 <= ny <= 500 and not visited[nx][ny] and not lst[nx][ny]:
                visited[nx][ny] = True
                qu.append([nx, ny, cnt + 1])


# 목적지 좌표, 웅덩이 개수
X, Y, N = map(int, stdin.readline().split())
pool = [list(map(int, stdin.readline().split())) for _ in range(N)]
lst = [[0] * 1001 for _ in range(1001)]

# 맵에 웅덩이 표시
for px, py in pool:
    lst[px][py] = 1

visited = [[False] * 1001 for _ in range(1001)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = float('inf')
bfs()

print(res)
