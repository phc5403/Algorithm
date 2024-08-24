from sys import stdin


# 목표 운동 시간 / 맥박 최솟값 / 맥박 최댓값 / 운동+ / 휴식-
N, minimum, maximum, train, rest = map(int, stdin.readline().split())
cnt = 0  # 현재 운동한 횟수
time = 0  # 시간
pulse = minimum  # 맥박

while cnt < N:
    if minimum + train > maximum:
        break

    if pulse + train <= maximum:
        pulse += train
        cnt += 1

    elif pulse - rest >= minimum:
        pulse -= rest

    elif pulse - rest < minimum:
        pulse = minimum

    time += 1

if cnt == N:
    print(time)
else:
    print(-1)
