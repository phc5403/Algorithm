from sys import stdin


for tc in range(1, 4):
    N = int(stdin.readline())

    lst = [int(stdin.readline()) for _ in range(N)]

    res = sum(lst)

    if res == 0:
        print(0)
    elif res > 0:
        print('+')
    else:
        print('-')