from sys import stdin
from collections import deque
from pprint import pprint


def bfs(start_x, start_y):
    global ex, ey

    qu = deque([[start_x, start_y, 0, [[start_x, start_y]]]])
    visited[start_x][start_y] = 1

    while qu:
        x, y, cnt, dist = qu.popleft()
        # print(qu)

        # END
        if [x, y] == [ex, ey]:
            # print(dist)
            return cnt, dist

        for k in range(4):
            nx = x
            ny = y

            while 1:
                nx += dx[k]
                ny += dy[k]

                if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    next_dist = dist + [[nx, ny]]
                    qu.append([nx, ny, cnt + 1, next_dist])
                else:
                    break

    return "Impossible", []


TC = int(stdin.readline())

for tc in range(1, TC + 1):
    sy, sx, ey, ex = stdin.readline().strip().split()
    lst = [[0] * 8 for _ in range(8)]
    visited = [[0] * 8 for _ in range(8)]

    sy, ey = ord(sy) - 65, ord(ey) - 65
    sx, ex = 8 - int(sx), 8 - int(ex)

    # 좌상 우상 우하 좌하
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]

    res, distance = bfs(sx, sy)
    if res != "Impossible":
        print(res, end=' ')
    else:
        print(res)

    for rx, ry in distance:
        print(chr(ry + 65), 8 - rx, end=' ')


'''
1
F 1 E 8

START
(7, 5) -> (3, 1) -> (0, 4)
'''