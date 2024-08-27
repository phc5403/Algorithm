from sys import stdin
import math

TC = int(stdin.readline())

for _ in range(1, TC + 1):
    a, b = map(int, stdin.readline().split())

    print(math.lcm(a, b), end=' ')
    print(math.gcd(a, b))