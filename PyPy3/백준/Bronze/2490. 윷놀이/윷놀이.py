from sys import stdin, stdout
from collections import deque
import sys

lst = [list(map(int, stdin.readline().split()))for _ in range(3)]

for i in range(len(lst)):
    if lst[i].count(0) == 1:
        print("A")
    elif lst[i].count(0) == 2:
        print("B")
    elif lst[i].count(0) == 3:
        print("C")
    elif lst[i].count(0) == 4:
        print("D")
    else:
        print("E")
