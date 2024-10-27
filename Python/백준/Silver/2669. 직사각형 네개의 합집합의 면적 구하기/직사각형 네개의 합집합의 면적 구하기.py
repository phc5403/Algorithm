from sys import stdin

lst = []
res = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    lst.append([x1, y1, x2, y2])


rectangle = [[0] * 101 for _ in range(101)]

for x1, y1, x2, y2 in lst:
    for x in range(x1, x2):
        for y in range(y1, y2):
            rectangle[x][y] = 1

for row in range(101):
    for col in range(101):
        if rectangle[row][col]:
            res += 1

print(res)