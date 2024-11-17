from sys import stdin

string = list(stdin.readline().strip())
T = int(stdin.readline())

for _ in range(T):
    A, B = map(int, stdin.readline().split())

    temp = string[A]
    string[A] = string[B]
    string[B] = temp

print(*string, sep='')