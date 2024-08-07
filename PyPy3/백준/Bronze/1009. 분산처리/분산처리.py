from sys import stdin

TC = int(stdin.readline())

for tc in range(1, TC + 1):
    a, b = map(int, stdin.readline().split())

    res = a

    for i in range(2, b+1):
        res = (res * a) % 10

    if b == 1:
        res = a % 10

    if res == 0:
        res = 10

    print(res)
