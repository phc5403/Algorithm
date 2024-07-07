from sys import stdin, stdout
from collections import deque
import copy


def rainny(rain):  # 비가 내리고 잠긴 후의 lst를 넘기기.
    temp = copy.deepcopy(lst)  # 깊은 복사

    for a in range(N):
        for b in range(N):
            if temp[a][b] <= rain:
                temp[a][b] = 0

    return temp


def bfs(start_x, start_y):
    global tmp
    qu = deque()
    qu.append([start_x, start_y]) 

    while qu:
        x, y = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if tmp[nx][ny]:
                tmp[nx][ny] = 0
                qu.append([nx, ny])
    return


# 2 <= N <= 100
N = int(stdin.readline())

# 1 <= element <= 100
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]

idx = 0
for p in range(N):
    for q in range(N):
        if idx < lst[p][q]:
            idx = lst[p][q]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 비가 0(내리지않음)이면, 최대 구역 = 1
res = [1]

for r in range(1, idx):  # 비가 1 ~ 100까지 내리는 경우 순회
    tmp = rainny(r)  # 비에 잠긴 후의 lst
    cnt = 0

    for s in range(N):
        for e in range(N):
            if tmp[s][e]:
                bfs(s, e)
                cnt += 1
    res.append(cnt)

print(max(res))
