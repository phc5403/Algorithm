from sys import stdin

N = int(stdin.readline())
name = stdin.readline().strip()

lst = list(name)
res = 0

for i in lst:
    res += ord(i) - 64

print(res)