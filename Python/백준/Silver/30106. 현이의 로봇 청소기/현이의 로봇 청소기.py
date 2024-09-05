import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    # 현재 위치를 방문했음을 표시
    vis[x][y] = 1

    q = deque([(x, y)])
    while q:
        r, c = q.popleft()

        # 상하좌우 네 방향에 대해 검사
        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + i[0]
            nc = c + i[1]

            # 새로운 위치가 유효한 범위 내에 있고, 방문하지 않았으며, 높이 차이가 k 이하인 경우
            if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc]:
                if abs(room[r][c] - room[nr][nc]) <= k:
                    vis[nr][nc] = 1
                    q.append((nr, nc))


n, m, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
vis = [[0]*m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            bfs(i, j)
            ans += 1

print(ans)