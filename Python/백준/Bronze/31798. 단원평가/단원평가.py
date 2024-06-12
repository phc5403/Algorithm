from sys import stdin

#  원 위의 두 수를 합하면 원 아래 수의 제곱.

a, b, c = map(int, stdin.readline().split())

if a == 0:
    print(c ** 2 - b)
elif b == 0:
    print(c ** 2 - a)
elif c == 0:
    print(int((a + b) ** (1/2)))
