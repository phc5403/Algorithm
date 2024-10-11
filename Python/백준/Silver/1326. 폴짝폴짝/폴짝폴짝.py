from sys import stdin
from collections import deque


def bfs(sx):
    global res, end

    qu = deque()
    visited = [False] * N
    qu.append([sx, 0])
    visited[sx] = True

    while qu:
        x, cnt = qu.popleft()  # 현재 위치, 점프 횟수

        # END
        if x == end:
            return cnt

        jump = lst[x]  # 점프할 위치 계산
        
        # 1. 오른쪽으로 점프
        for nx in range(x + jump, N, jump):
            if not visited[nx]:
                visited[nx] = True
                qu.append([nx, cnt + 1])

        # 2. 왼쪽으로 점프
        for nx in range(x - jump, -1, -jump):
            if not visited[nx]:
                visited[nx] = True
                qu.append([nx, cnt + 1])

    return -1

N = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
start, end = map(int, stdin.readline().split())
start -= 1  # 리스트 index 조절을 위해 차감
end -= 1  # 리스트 index 조절을 위해 차감

res = bfs(start)
print(res)