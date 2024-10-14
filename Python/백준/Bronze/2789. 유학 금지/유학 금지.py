from sys import stdin

string = stdin.readline().strip()
censorship = sorted(list("CAMBRIDGE"))
res = ""

for s in string:
    if s not in censorship:
        res += s

print(res)