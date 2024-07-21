from sys import stdin

lst = [0] * 101

lst[1], lst[2], lst[3] = 1, 1, 1
lst[4], lst[5] = 2, 2

for i in range(6, 101):
    lst[i] = lst[i-1] + lst[i-5]

N = int(stdin.readline())
for a in range(N):
    num = int(stdin.readline())
    print(lst[num])