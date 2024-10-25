from sys import stdin

cnt = 0

while True:
    line = stdin.readline()

    if line == '':
        break

    cnt += 1

print(cnt)