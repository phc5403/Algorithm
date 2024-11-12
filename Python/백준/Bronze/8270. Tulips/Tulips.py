from sys import stdin

N = int(stdin.readline())
tulips = list(map(int, stdin.readline().split()))
cnt = [0] * 15000

for t in tulips:
    cnt[t - 1] += 1

print(cnt.count(0))
