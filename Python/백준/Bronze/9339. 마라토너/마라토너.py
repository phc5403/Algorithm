from sys import stdin

TC = int(stdin.readline())

for tc in range(1, TC + 1):
    K = int(stdin.readline())  # 수강생의 수
    student = list(map(int, stdin.readline().split()))  # 수강생 번호
    N = int(stdin.readline())  # 모든 참가자 수
    lst = [list(map(int, stdin.readline().split())) for _ in range(N)]  # 모든 참가자 정보

    res = []  # 수강생 정보를 새로 조정하여 담을 리스트
    most_stu = 0  # 가장 기록이 좋은 수강생
    certificate = 0  # 인증서를 받은 수강생의 수

    for num, hour, minute in lst:
        # 1. 수강생이 아닌 경우 제외
        if num not in student:
            continue

        # 2. 중도 포기 제외
        if hour == -1 or minute == -1:
            continue

        # 3. 기록이 6시간 초과일 경우 제외
        time = (hour * 60) + minute
        if time > 360:
            continue

        res.append([num, time])  # [수강생 번호, 완주 시간]

    # 수강생의 기록순으로 정렬
    res.sort(key=lambda x: x[1])

    most_stu = res[0][0]
    certificate = len(res)
    print(most_stu, certificate)
