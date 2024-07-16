from sys import stdin
from collections import deque
from pprint import pprint
import sys
sys.setrecursionlimit(100000)

N = int(stdin.readline())  # 7

tree = [[] for _ in range(N+1)]  # 8
parent = [[] for _ in range(N+1)]  # 2번 노드부터 순서대로 출력
visited = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# print(tree)  # [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
# print(visited)


def dfs_tree(start):
    global parent
    visited[start] = True
    stack.append(start)  # 처음 루트 1번 노드 넣고 시작.

    while stack:  # 스택이 빌 때 까지 == 모든 정점이 visited 될 때 까지.

        node = stack.pop()

        for child in tree[node]:  # 1: (6, 4)
            if not visited[child]:
                parent[child].append(node)  # parent[자식] = 부모
                dfs_tree(child)

    return


stack = []
dfs_tree(1)
#                         1   2    3    4    5    6    7   
# print(parent)  # [[x], [], [4], [6], [1], [3], [1], [4]] -> parent[자식] = 부모

for x in range(2, len(parent)):
    print(parent[x][0])