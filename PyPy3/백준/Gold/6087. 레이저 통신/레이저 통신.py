from sys import stdin, stdout
from collections import deque
from pprint import pprint
import heapq
import copy


def bfs(start_x, start_y):
    qu = deque()
    visited = [[False] * W for _ in range(H)]
    lst[start_x][start_y] = "S"
    visited[start_x][start_y] = True
    mirror = -1
    qu.append([start_x, start_y, mirror])

    while qu:
        x, y, mr = qu.popleft()

        if lst[x][y] == 'C':
            return print(mr)

        for k in range(4):
            nx = x
            ny = y

            while True:  # 1. 한 방향씩 잡고 쭉 밀기
                nx += dx[k]
                ny += dy[k]

                # print(f"NX, NY = {nx}, {ny}")

                # 1-1. 갈 수 있는 범위면 한 방향으로 밀기
                if 0 <= nx <= H - 1 and 0 <= ny <= W - 1:
                    # 가다가 벽 만나면 끝냄 -> (다음 방향 준비)
                    if lst[nx][ny] == '*':
                        break

                    # 한 방향 밀면서 방문 안한곳이면
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        qu.append([nx, ny, mr + 1])

                # 1-2. 갈 수 없는 범위면 다음 끝내고 다음 방향.
                else:
                    break


# 7, 8
W, H = map(int, stdin.readline().split())

lst = [list(stdin.readline().strip()) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 출발 & 도착 좌표
s_x, s_y = 0, 0

for row in range(H):
    for col in range(W):
        if lst[row][col] == 'C':
            if not s_x and not s_y:
                s_x, s_y = row, col
                break

bfs(s_x, s_y)