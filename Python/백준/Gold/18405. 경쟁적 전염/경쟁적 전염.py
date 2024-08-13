from sys import stdin
from collections import deque
from pprint import pprint

N, K = map(int, stdin.readline().split())
lst = []  # 맵
virus = []  # 바이러스 정보
visited = [[0] * N for _ in range(N)]  # 방문 처리

for r in range(N):
    lst.append(list(map(int, stdin.readline().split())))
    for c in range(N):
        if lst[r][c]:
            virus.append([lst[r][c], 0, r, c])  # [바이러스 종류, 시간, X 좌표, Y 좌표]
            visited[r][c] = 1

S, X, Y = map(int, stdin.readline().split())

# 바이러스를 낮은 종류순으로 정렬
virus.sort(key=lambda x: x[0])
qu = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while qu:
    num, second, x, y = qu.popleft()

    # END : 정해진 시간 이후 좌표 출력
    if second == S:
        break

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 바이러스 종류가 낮은 순으로 순회하므로, 방문 안된 곳(현재 빈 칸)만 확인하기 위함.
        # 이렇게하면, 최초 빈 칸이었다가 다른 바이러스로 채워졌을 경우에도 순회하지 않음.
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            lst[nx][ny] = num  # 바이러스 증식
            qu.append([num, second + 1, nx, ny])

print(lst[X - 1][Y - 1])
