from sys import stdin
from collections import deque

N = int(stdin.readline())
qu = deque()

for _ in range(N):
    oper = list(map(int, stdin.readline().split()))

    if oper[0] == 1:
        qu.appendleft(oper[1])

    elif oper[0] == 2:
        qu.append(oper[1])

    elif oper[0] == 3:
        if qu:
            print(qu.popleft())
        else:
            print(-1)

    elif oper[0] == 4:
        if qu:
            print(qu.pop())
        else:
            print(-1)

    elif oper[0] == 5:
        print(len(qu))

    elif oper[0] == 6:
        if qu:
            print(0)
        else:
            print(1)

    elif oper[0] == 7:
        if qu:
            print(qu[0])
        else:
            print(-1)

    elif oper[0] == 8:
        if qu:
            print(qu[-1])
        else:
            print(-1)