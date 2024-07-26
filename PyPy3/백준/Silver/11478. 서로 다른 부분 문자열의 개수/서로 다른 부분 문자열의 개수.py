import sys

input = sys.stdin.readline()

# ababc
s = input.strip()

sett = set()

for x in range(len(s)):  # 0 1 2 3 4
    for y in range(x, len(s)):  # 0 1 2 3 4
        sett.add(s[x:y+1])

print(len(sett))

