from sys import stdin

N = int(stdin.readline())
res = 0

for _ in range(N):
    bill, temp = map(int, stdin.readline().split())
    
    if bill == 136:
        res += 1000
    elif bill == 142:
        res += 5000
    elif bill == 148:
        res += 10000
    else:
        res += 50000

print(res)