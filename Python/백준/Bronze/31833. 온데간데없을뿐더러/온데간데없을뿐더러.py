from sys import stdin

N = int(stdin.readline())
A = list(stdin.readline().split())
B = list(stdin.readline().split())

A = int(''.join(A))
B = int(''.join(B))

print(min(A, B))
