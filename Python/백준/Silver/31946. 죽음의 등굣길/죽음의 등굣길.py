from sys import stdin
from collections import deque


def bfs():
    qu = deque([[0, 0]])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    color = lst[0][0]  # 현재 보도블럭 색상

    while qu:
        x, y = qu.popleft()

        if [x, y] == [N - 1, M - 1]:
            return "ALIVE"

        for dx in range(-jump, jump + 1):
            for dy in range(-jump, jump + 1):
                if abs(dx) + abs(dy) <= jump:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and color == lst[nx][ny]:
                        visited[nx][ny] = True
                        qu.append([nx, ny])

    return "DEAD"


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


N = int(stdin.readline())
M = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]
jump = int(stdin.readline())

res = bfs()
print(res)