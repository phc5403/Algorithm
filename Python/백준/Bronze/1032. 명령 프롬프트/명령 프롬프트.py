from sys import stdin

N = int(stdin.readline())
lst = list(stdin.readline().strip())

for _ in range(N-1):
    compare = list(stdin.readline().strip())
    for idx in range(len(compare)):
        if lst[idx] == compare[idx]:
            continue
        else:
            lst[idx]='?'

print(*lst, sep="")