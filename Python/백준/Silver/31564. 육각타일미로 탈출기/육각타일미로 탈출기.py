from sys import stdin
from collections import deque
from pprint import pprint


def bfs():
    qu = deque()
    qu.append([0, 0, 0])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    # 장애물 -> 방문 처리(접근 하지 못함)
    for block_x, block_y in block:
        visited[block_x][block_y] = 1

    while qu:
        x, y, cnt = qu.popleft()

        # END : 목적지 도착
        if [x, y] == [N - 1, M - 1]:
            return cnt

        for k in range(6):
            if x % 2 == 0:  # 현재 위치가 짝수행일 경우.
                nx = x + dx_even[k]
                ny = y + dy_even[k]
            else:  # 현재 위치가 홀수행일 경우.
                nx = x + dx_odd[k]
                ny = y + dy_odd[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                qu.append([nx, ny, cnt + 1])

    return -1


N, M, K = map(int, stdin.readline().split())
block = [list(map(int, stdin.readline().split())) for _ in range(K)]

# 짝수 : 좌하 / 하 / 우 / 상 / 좌상 / 좌
dx_even = [-1, -1, 0, 1, 1, 0]
dy_even = [-1, 0, 1, 0, -1, -1]

# 홀수 : 하 / 우하 / 우 / 우상 / 상 / 좌
dx_odd = [-1, -1, 0, 1, 1, 0]
dy_odd = [0, 1, 1, 1, 0, -1]

res = bfs()
print(res)


'''
1. 짝수행(2, 2) 기준
좌하 / 하 / 우 / 상 / 좌상 / 좌

2. 홀수행(1, 1) 기준 
하 / 우하 / 우 / 우상 / 상 / 좌
'''