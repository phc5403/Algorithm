from sys import stdin

N, K = map(int, stdin.readline().split())

for _ in range(N-1):
    K //= 2

print(K)