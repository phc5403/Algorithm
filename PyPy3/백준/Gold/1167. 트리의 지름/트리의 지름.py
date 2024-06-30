from sys import stdin
from collections import deque

V = int(stdin.readline())

tree = [[] for _ in range(V+1)]
visited = [False] * (V+1)
dist = [0] * (V+1)

for _ in range(V):
    s = list(map(int, stdin.readline().split()))  # [1, 3, 2, -1]

    for j in range(1, len(s)-1, 2):
        tree[s[0]].append((s[j], s[j+1]))


def bfs_dist(start):
    visited[start] = True
    qu.append(start)

    while qu:
        node = qu.popleft()

        for nxt in tree[node]:
            if not visited[nxt[0]]:
                visited[nxt[0]] = True
                qu.append(nxt[0])
                dist[nxt[0]] = dist[node] + nxt[1]

    return


qu = deque()
bfs_dist(1)  # 1회차

tmp = dist.index(max(dist))

visited = [False] * (V+1)
dist = [0] * (V+1)

bfs_dist(tmp)
print(max(dist))

