from sys import stdin

N, M = map(int, stdin.readline().split())
res = 0

for _ in range(N):
    string = stdin.readline().strip()

    cnt = 0
    for s in string:
        if s == 'O':
            cnt += 1

    if cnt > (M //2):
        res += 1

print(res)