from sys import stdin, stdout
import sys

N = int(stdin.readline())

res = []
lst = []

for _ in range(N):
    name, day, month, year = stdin.readline().split()
    lst.append((name, int(year), int(month), int(day)))

res = sorted(lst, key=lambda x: (-x[1], -x[2]))
print(res[0][0])
res = sorted(lst, key=lambda x: (x[1], x[2]))
print(res[0][0])