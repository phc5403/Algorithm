from sys import stdin
from collections import deque
from pprint import pprint
import time


def bfs(s_x, s_y):
    global maze

    qu = deque()
    visited = [[False] * W for _ in range(H)]
    visited[s_x][s_y] = True
    qu.append([s_x, s_y])
    cnt = 1

    while qu:
        qu_len = len(qu)
        fired_len = len(fired)

        for _ in range(fired_len):
            fx, fy = fired.popleft()
            for z in range(4):
                nfx = fx + dx[z]
                nfy = fy + dy[z]

                if 0 <= nfx < H and 0 <= nfy < W and maze[nfx][nfy] == '.':
                    maze[nfx][nfy] = 'F'
                    fired.append([nfx, nfy])

        for _ in range(qu_len):
            jx, jy = qu.popleft()

            for k in range(4):
                njx = jx + dx[k]
                njy = jy + dy[k]

                # njx, njy가 갈 수 있는 곳 조사
                if 0 <= njx < H and 0 <= njy < W and maze[njx][njy] == '.' and not visited[njx][njy]:

                    # << END_Condition >> #
                    if njx + dx[k] < 0 or njx + dx[k] >= H or njy + dy[k] < 0 or njy + dy[k] >= W:
                        print(cnt + 1)
                        return

                    visited[njx][njy] = True
                    qu.append([njx, njy])
        cnt += 1
    print("IMPOSSIBLE")
    return

TC = int(stdin.readline())
for tc in range(TC):
    W, H = map(int, stdin.readline().split())

    maze = [list(stdin.readline().strip()) for _ in range(H)]

    fired = deque()
    start_jx, start_jy = 0, 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start = time.time()  ###

    for row in range(H):
        for col in range(W):
            if maze[row][col] == '@':
                maze[row][col] = '.'
                start_jx, start_jy = row, col

            if maze[row][col] == '*':
                fired.append([row, col])

    if start_jx == 0 or start_jx == H-1 or start_jy == 0 or start_jy == W-1:
        print(1)
    else:
        bfs(start_jx, start_jy)

    end = time.time()  ###
    # print(f'{end - start:.3f} sec / {round((end - start) * 1000)} ms')
