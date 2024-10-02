from sys import stdin

N = int(stdin.readline())

lst = list(map(int, stdin.readline().split()))
lst.sort()
print(lst[-1])