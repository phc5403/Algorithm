from sys import stdin

lst = [list(map(int, stdin.readline().split())) for _ in range(3)]

for i in range(3):
    start_hour, start_min, start_second, end_hour, end_min, end_second = lst[i]

    # 초로 변환
    start_time = (start_hour * 3600) + (start_min * 60) + start_second
    end_time = (end_hour * 3600) + (end_min * 60) + end_second

    res = end_time - start_time
    print(res // 3600, (res % 3600) // 60, (res % 3660) % 60)
