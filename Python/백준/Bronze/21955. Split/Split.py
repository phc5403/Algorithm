from sys import stdin

N = stdin.readline().strip()
length = int(len(N) / 2)

print(N[0:length], N[length:])
