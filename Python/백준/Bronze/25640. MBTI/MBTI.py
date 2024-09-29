from sys import stdin

string = stdin.readline().strip()

N = int(stdin.readline())
res = 0

for _ in range(N):
    if  string == stdin.readline().strip():
        res += 1

print(res)