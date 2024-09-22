from sys import stdin

lst = list(map(int, stdin.readline().split()))
print(lst[0] * lst[1] - lst[2] * lst[3] * lst[4])