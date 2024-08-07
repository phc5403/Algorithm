from sys import stdin

TC = int(stdin.readline().strip())

for tc in range(1, TC + 1):
    a, b = map(int, stdin.readline().split())

    res = 1

    for i in range(b):
        res = (res * a) % 10

    if res == 0:
        res = 10

    print(res)
