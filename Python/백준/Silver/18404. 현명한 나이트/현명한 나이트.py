from sys import stdin
from collections import deque
from pprint import pprint


def bfs(sx, sy):
    qu = deque()
    qu.append([sx, sy, 0])
    visited[sx][sy] = True

    while qu:
        x, y, cnt = qu.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                qu.append([nx, ny, cnt + 1])

                if lst[nx][ny] and [nx, ny] in enemy:
                    res[enemy.index([nx, ny])] = cnt + 1


N, M = map(int, stdin.readline().split())
knight_x, knight_y = map(int, stdin.readline().split())  # 인덱스 -1 처리
enemy = [list(map(int, stdin.readline().split())) for _ in range(M)]  # 인덱스 -1 처리
lst = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
res = [0] * M

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for idx in range(M):
    enemy[idx][0], enemy[idx][1] = enemy[idx][0] - 1, enemy[idx][1] - 1

for ex, ey in enemy:
    lst[ex][ey] = 1

bfs(knight_x - 1, knight_y - 1)
print(*res)

'''
M개의 말 각각 도달하는 위치를 찾아야 함.
즉, 정답도 M개.
'''