from sys import stdin
import sys
from collections import deque
sys.setrecursionlimit(10**5)

# 정점 수, 간선 수, 시작 정점
N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
R = 1

edge = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    edge[x].append(y)
    edge[y].append(x)

# print(edge)

visited = [0] * (N+1)
# res = [0] * (N+1)
path = []
qu = deque()
cnt = 0  # 감염된 수.


def dfs_computers(start):  # Depth First Search(깊이 우선 탐색)
    global cnt
    visited[start] = 1
    path.append(start)
    qu.append(start)

    while qu:
        tmp = qu.pop()

        for node in edge[tmp]:
            if not visited[node]:
                cnt += 1
                visited[node] = 1
                qu.append(node)
                path.append(node)
    return


dfs_computers(R)

print(cnt)
