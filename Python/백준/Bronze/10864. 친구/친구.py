from sys import stdin

N, M = map(int, stdin.readline().split())

lst = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, stdin.readline().split())

    lst[a - 1].append(b)
    lst[b - 1].append(a)

for i in range(N):
    print(len(lst[i]))