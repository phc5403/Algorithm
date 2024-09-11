from sys import stdin
from collections import deque


def bfs():
    global A, B, N, M, res

    qu = deque()
    qu.append([N, 0])
    visited[N] = True

    while qu:
        x, cnt = qu.popleft()

        if res < cnt:
            continue

        if x == M:
            res = min(res, cnt)

        for dx in [1, -1, -A, A, -B, B, x * (A - 1), x * (B - 1)]:
            nx = x + dx

            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                qu.append([nx, cnt + 1])


A, B, N, M = map(int, stdin.readline().split())
visited = [False] * 100001
res = float('inf')
bfs()
print(res)
