from sys import stdin
from collections import deque


def bfs(sx, sy):
    qu = deque()
    qu.append([sx, sy])
    visited[sx][sy] = 1
    color = A[sx][sy]  # 현재 구역의 색

    # B와 색을 검증하기 위해 탐색한 좌표를 저장하는 Queue
    dist = deque()
    dist.append([sx, sy])

    while qu:
        x, y = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and color == A[nx][ny]:
                visited[nx][ny] = 1

                dist.append([nx, ny])
                qu.append([nx, ny])

    return dist


def verification_colors(queue):
    # 큐의 첫 원소좌표에 해당하는 B의 색상값 저장
    color_B = B[queue[0][0]][queue[0][1]]

    while queue:
        bx, by = queue.popleft()

        # 앞서 탐색했던 A의 구역 좌표를 순회하면서, B의 색상들이 모두 같은지 검증
        if color_B != B[bx][by]:
            return False

    return True


N, M = map(int, stdin.readline().split())
A = [list(stdin.readline().strip()) for _ in range(N)]
B = [list(stdin.readline().strip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = "YES"

for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            check = bfs(n, m)
            
            if not verification_colors(check):
                res = "NO"

print(res)

'''
반례
2 4
AAAA
BBBB
AAAA
AAAA

answer = YES
'''
