from collections import deque
from sys import stdin

N = int(stdin.readline())
qu = deque(enumerate(map(int, stdin.readline().split())))
res = []

while qu:
    idx, nxt = qu.popleft()

    if nxt > 0:
        qu.rotate(-(nxt - 1))

    elif nxt < 0:
        qu.rotate(-nxt)

    res.append(idx + 1)

print(*res)