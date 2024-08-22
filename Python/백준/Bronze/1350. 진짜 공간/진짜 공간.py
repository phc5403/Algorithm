from sys import stdin
import math

N = int(stdin.readline())
files = list(map(int, stdin.readline().split()))
cluster = int(stdin.readline())

disk = []
res = 0

for file in files:
    disk.append(math.ceil(file / cluster))

for i in disk:
    res += i * cluster

print(res)