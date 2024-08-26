from sys import stdin
import math

'''
# A**2 + B**2 = C**2

1. (height*x)^2+(width*x)^2=len^2
2. (height^2+width^2)*x^2=len^2
3. x=len/(height^2+width^2)^(1/2)

'''

D, H, W = map(int, stdin.readline().split())

x = D / math.sqrt(math.pow(H, 2) + math.pow(W, 2))

print(f"{int(H * x)} {int(W * x)}")