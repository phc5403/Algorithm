from sys import stdin
from collections import deque
from pprint import pprint
# https://www.acmicpc.net/problem/2206 -> 문제
# https://seongonion.tistory.com/m/107 -> 해설


def bfs_maze():
    qu.append([0, 0, 0])
    visited[0][0][0] = 1

    while qu:
        # print(qu)
        x, y, h = qu.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][h]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 1. 좌표상 오류가 없을 때,
            if 0 <= nx < N and 0 <= ny < M:
                # 1-1. 벽X / 방문 X
                if not maze[nx][ny] and not visited[nx][ny][h]:
                    # maze[nx][ny] = maze[x][y] + 1
                    visited[nx][ny][h] = visited[x][y][h] + 1
                    qu.append([nx, ny, h])

                # 1-2. 벽O / Crash OFF
                elif maze[nx][ny] and not h:
                    # 벽을 부숨 -> [h+1] == [1]
                    visited[nx][ny][h+1] = visited[x][y][h] + 1
                    qu.append([nx, ny, h+1])

    # 아예 갈 수가 없으면 -1.
    return -1


N, M = map(int, stdin.readline().split())

# 0 = 이동 가능 / 1 = 벽
maze = [list(map(int, stdin.readline().strip())) for _ in range(N)]

# visitied[x][y][z] / z = 0 or 1
# z=0 벽을 뚫지않고 감 / z=1 벽을 뚫고 감
visited = [[[0]*2 for _ in range(M)] for __ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

qu = deque()

print(bfs_maze())

# print(f'\n최종 maze, visited 점검')
# pprint(maze, width=40)
# pprint(visited, width=50)

