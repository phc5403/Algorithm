from sys import stdin

N = int(stdin.readline())
K = 1  # 노래 할 자연수
cnt = 0  # 경과시간

while N:
    if N < K:
        K = 1

    else:
        N -= K
        K += 1
        cnt += 1


print(cnt)
