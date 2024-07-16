from sys import stdin
from collections import deque
from pprint import pprint

TC = int(stdin.readline())

for _ in range(TC):

    # N x N 체스판 크기
    N = int(stdin.readline())

    # 현재 좌표 / 목표 좌표
    cur_x, cur_y = map(int, stdin.readline().split())
    mov_x, mov_y = map(int, stdin.readline().split())
    
    # 체스판 / 방문판
    chess = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 8방향 이동 (왼쪽 위부터 시계방향)
    dx = [-1, -2, -2, -1, +1, +2, +2, +1]
    dy = [-2, -1, +1, +2, +2, +1, -1, -2]
    # cnt = 0

    # print(N)
    # print(cur_x, cur_y)
    # print(mov_x, mov_y)
    # pprint(lst, width=40)
    # pprint(visited, width=60)


    def bfs_chess(start_x, start_y):
        visited[start_x][start_y] = True
        qu = deque()
        qu.append([start_x, start_y])

        while qu:
            x, y = qu.popleft()
            # print(f'x, y={x}, {y}')

            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                # print(f'nx,ny={nx}, {ny}')

                if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                    continue

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    chess[nx][ny] = chess[x][y] + 1
                    qu.append([nx, ny])

                    if nx == mov_x and ny == mov_y:
                        break

        return chess[mov_x][mov_y]


    # bfs_chess(cur_x, cur_y)
    print(bfs_chess(cur_x, cur_y))
    # pprint(chess, width=40)
    # pprint(visited, width=60)