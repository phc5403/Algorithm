from sys import stdin
from collections import deque

# 0 <= N <= 1,000,000
N = stdin.readline().strip()
room = []

for j in range(len(N)):
    room.append(int(N[j]))

res = 0

while room:
    check = [False for _ in range(10)]
    temp = room[:]

    for i in temp:
        if not check[i]:
            check[i] = True
            room.pop(room.index(i))

        elif i == 6 and check[6] and not check[9]:
            check[9] = True
            room.pop(room.index(i))

        elif i == 9 and check[9] and not check[6]:
            check[6] = True
            room.pop(room.index(i))

    res += 1

print(res)

