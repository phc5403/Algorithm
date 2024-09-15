from sys import stdin
from collections import deque
from pprint import pprint


def bfs(sx, sy):
    global res

    qu = deque()
    qu.append([sx, sy, 1])
    visited[sx][sy] = 1

    while qu:
        x, y, cnt = qu.popleft()
        boost = lst[x][y]

        # print(x, y, boost, cnt)

        # 가지치기
        if res < cnt:
            continue

        # 종료 조건 : 도착
        if [x, y] == [N - 1, M - 1]:
            res = min(res, cnt - 1)

        for boot in range(1, boost + 1):
            nx = x + boot

            if 0 <= nx < N and 0 <= y < M and not visited[nx][y]:
                visited[nx][y] = 1
                qu.append([nx, y, cnt + 1])

        for boot in range(1, boost + 1):
            ny = y + boot

            if 0 <= x < N and 0 <= ny < M and not visited[x][ny]:
                visited[x][ny] = 1
                qu.append([x, ny, cnt + 1])




N, M = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

res = float('inf')

bfs(0, 0)
print(res)

'''
1. 오른쪽으로 최대 x칸
2. 아래쪽으로 최대 x칸
3. 이동 중, 부스트 습득 불가
4. 이동 후 멈추면서, 보유하고 있던 부스터는 모두 소진.
'''