from sys import stdin, stdout
from collections import deque


def bfs(n1, n2):
    # 출발, 목적지
    start, end = min(n1, n2), max(n1, n2)
    qu = deque()
    visited[start] = 1
    qu.append(start)
    cnt = 0

    while qu:
        cur = qu.popleft()
        # print(f'cur={cur}, cnt={cnt}')

        for nxt in edge[cur]:
            if nxt == end:
                visited[nxt] = visited[cur] + 1
                # print(visited)
                return visited[nxt]-1

            if not visited[nxt]:
                # visited[nxt] = True
                visited[nxt] = visited[cur] + 1
                qu.append(nxt)
                # cnt += 1
                # print(f'nxt={nxt}, cnt={cnt}')


# 사람들 번호
N = int(stdin.readline())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
num1, num2 = map(int, stdin.readline().split())

M = int(stdin.readline())

edge = [[] for _ in range(N+1)]
visited = [0] * (N+1)
# print(visited)

for _ in range(M):
    # a = b의 부모 번호, 부모는 최대 1명 주어짐.
    a, b = list(map(int, stdin.readline().split()))
    edge[a].append(b)
    edge[b].append(a)

# print(edge)

res = bfs(num1, num2)
# print(f'res = {res}')

if res is None:
    print(-1)
else:
    print(res)
