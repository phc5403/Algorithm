from sys import stdin
from collections import deque


def dfs(x, y, nums):
    global res

    if len(nums) == 6:
        res.add(nums)
        return

    nums += str(lst[x][y])

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, nums)


lst = [list(map(int, stdin.readline().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = set()

for r in range(5):
    for c in range(5):
        dfs(r, c, "")

print(len(res))