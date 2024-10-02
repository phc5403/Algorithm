from sys import stdin

N = int(stdin.readline())
res = ''


for _ in range(N):
    string = stdin.readline().strip()

    for s in string:
        if s == 'S':
            res = string
            break

print(res)
