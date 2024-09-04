from sys import stdin

N = int(stdin.readline())
menu = [int(stdin.readline()) for _ in range(N)]

M = int(stdin.readline())
saenaegi = [int(stdin.readline()) for _ in range(M)]

res = 0

for idx in saenaegi:
    res += menu[idx - 1]

print(res)