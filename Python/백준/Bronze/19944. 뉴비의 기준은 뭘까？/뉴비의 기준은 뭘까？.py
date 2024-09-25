from sys import stdin

N, M = map(int, stdin.readline().split())

res = ""

if M == 1 or M == 2:
    res = "NEWBIE!"

elif 2 < M <= N:
    res = "OLDBIE!"

else:
    res = "TLE!"

print(res)
