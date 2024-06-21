from sys import stdin
from collections import deque
from pprint import pprint


def bfs_maze(a, b):
    visited[a][b] = True  # 방문 한곳은 지도에서 0으로 바꿈
    qu.append([a, b])

    while qu:
        x, y = qu.popleft()  # 왜 pop은 안되고 popleft()로 해야할까?

        for k in range(4):  # 상 -> 하 -> 좌 -> 우
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or not maze[nx][ny] or visited[nx][ny]:
                continue

            if maze[nx][ny]:  # 다음 위치
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1
                qu.append([nx, ny])
                if maze[nx][ny] == maze[N-1][M-1]:  # 끝지점에 도달하면 탈출
                    break

    return maze[N-1][M-1]


N, M = map(int, stdin.readline().split())

maze = [list(map(int, stdin.readline().strip())) for _ in range(N)]


visited = [[False] * M for _ in range(N)]
qu = deque()


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs_maze(0, 0))
# pprint(maze, width=50)
# pprint(visited, width=50)
# print(visited[N-1][M-1])
