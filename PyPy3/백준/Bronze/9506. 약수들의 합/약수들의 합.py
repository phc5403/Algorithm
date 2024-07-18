from sys import stdin, stdout
import sys

while 1:
    n = int(stdin.readline())

    if n == -1:
        break

    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)

    if n == sum(lst):
        print(f'{n} = ', end='')
        for j in lst:
            print(f'{j}', end='')
            if j != lst[-1]:
                print(" + ", end='')
        print()
    else:
        print(f'{n} is NOT perfect.')




