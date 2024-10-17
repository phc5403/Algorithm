from sys import stdin

lst = list(map(int, stdin.readline().split()))
N = lst[-1]
lst.pop()
hab = sum(lst)

res = N * 4 - hab

if res < 0:
    print(0)
else:
    print(res)

