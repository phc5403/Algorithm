from sys import stdin

N = int(stdin.readline())

lst = []

for _ in range(N):
    lst.append(stdin.readline().strip()[0])

temp = set(lst)
res = []

for i in temp:
    if lst.count(i) >= 5:
        res.append(i)

if res:
    res.sort()
    print(''.join(res))
else:
    print("PREDAJA")