from sys import stdin

N, M, K = map(int, stdin.readline().split())

# 음수면 문제 풀이 최소값을 0으로.
mins = max(0, N - (M * K))
maxs = N - M * (K - 1) - 1

print(mins, maxs)