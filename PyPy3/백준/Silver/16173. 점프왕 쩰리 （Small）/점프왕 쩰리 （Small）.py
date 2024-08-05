from sys import stdin
from collections import deque


def bfs():
    qu = deque()
    qu.append([0, 0])
    visited[0][0] = True

    while qu:
        x, y = qu.popleft()
        jump = lst[x][y]

        if lst[x][y] == -1:
            return "HaruHaru"

        for k in range(2):
            nx = x + dx[k] * jump
            ny = y + dy[k] * jump

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                qu.append([nx, ny])

    return "Hing"


N = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]
dx = [0, 1]
dy = [1, 0]

visited = [[False] * N for _ in range(N)]

print(bfs())