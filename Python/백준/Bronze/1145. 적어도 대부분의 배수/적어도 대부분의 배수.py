from sys import stdin


lst = list(map(int, stdin.readline().split()))
N = 1

while 1:
    cnt = 0
    for i in lst:
        if N % i == 0:
            cnt += 1
    
    if cnt >= 3:
        print(N)
        break
        
    N += 1