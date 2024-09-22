from sys import stdin

target = stdin.readline().strip()
N = int(stdin.readline())
res = 0

for t in range(N):
    string = stdin.readline().strip()
    cnt = 0

    for s in range(len(string)):
        if target[s] == string[s]:
            cnt += 1
        else:
            break
    if cnt >= 5:
        res += 1
print(res)