from sys import stdin

lst = [stdin.readline().strip()[0] for _ in range(3)]

lst.sort()

if lst == ['k', 'l', 'p']:
    print("GLOBAL")
else:
    print("PONIX")