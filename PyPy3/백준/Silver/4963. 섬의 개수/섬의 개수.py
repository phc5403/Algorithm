from sys import stdin
from collections import deque
from pprint import pprint


def bfs(sx, sy):
    qu = deque()
    qu.append([sx, sy])
    visited[sx][sy] = True

    while qu:
        x, y = qu.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and lst[nx][ny]:
                visited[nx][ny] = True
                qu.append([nx, ny])


while 1:
    W, H = map(int, stdin.readline().split())
    if W == 0 and H == 0:
        break

    lst = [list(map(int, stdin.readline().split())) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    res = 0

    # 상 우상 우 우하 하 좌하 좌 좌상
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for row in range(H):
        for col in range(W):
            if lst[row][col] and not visited[row][col]:
                bfs(row, col)
                res += 1

    print(res)