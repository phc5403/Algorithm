from sys import stdin

N, M = map(int, stdin.readline().split())
number = list(map(int, stdin.readline().split()))
res = 1

for idx in range(len(number)):
    res *= number[idx]

res %= M
print(res)
