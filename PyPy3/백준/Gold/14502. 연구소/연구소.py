from sys import stdin
from pprint import pprint
from collections import deque
import time
import copy


def build_walls(w_cnt):
    global laboratory, safe_zone

    if w_cnt == 3:
        # pprint(laboratory, width=30)
        # print()
        bfs(safe_zone - 3)
        return

    for r in range(N):
        for c in range(M):
            if not laboratory[r][c]:
                laboratory[r][c] = 1
                build_walls(w_cnt + 1)
                laboratory[r][c] = 0


def bfs(sz):
    global laboratory, virus, res
    qu = copy.deepcopy(virus)
    temp = copy.deepcopy(laboratory)

    while qu:
        x, y = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not temp[nx][ny]:
                temp[nx][ny] = 2
                sz -= 1
                qu.append([nx, ny])

    res = max(res, sz)
    return


# 2 second, 512 MB
# 3 <= N, M <= 8
# 2 <= virus <= 10
N, M = map(int, stdin.readline().split())
laboratory = [list(map(int, stdin.readline().split())) for _ in range(N)]
# 12! = 4억 7900만 1600
# 최대 빈칸 = 62 -> 62 C 3 = 37820

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

start = time.time()  ##

virus = deque()
safe_zone = 0
for v1 in range(N):
    for v2 in range(M):
        if laboratory[v1][v2] == 2:
            virus.append([v1, v2])
        if not laboratory[v1][v2]:
            safe_zone += 1

# print(safe_zone)
build_walls(0)
# print(f'END = {res}')
print(res)

end = time.time()  ##
# print(f"{round(int(end - start) * 1000)} ms")
