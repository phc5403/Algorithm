from sys import stdin, stdout
import sys

# 1 <= S <= 4,294,967,295
S = int(stdin.readline())
res = []
num = 0

i = 1
cnt = 0
while 1:
    #print(num, i, cnt)
    if num + i == S:
        print(cnt + 1)
        break
        
    if num + i + (i+1) < S:
        num += i
        cnt += 1
        
    elif num + i + (i+1) == S:
        num += i + (i+1)
        print(cnt+2)
        break

    i += 1