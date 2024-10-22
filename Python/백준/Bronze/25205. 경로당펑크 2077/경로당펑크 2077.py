from sys import stdin

N = int(stdin.readline())
lst = list(stdin.readline().strip())

symbol = ['r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g']


if lst[-1] in symbol:
    print(1)
else:
    print(0)