from sys import stdin

N, M = map(int, stdin.readline().split())
helmet = max(list(map(int, stdin.readline().split())))
vest = max(list(map(int, stdin.readline().split())))

print(helmet + vest)
