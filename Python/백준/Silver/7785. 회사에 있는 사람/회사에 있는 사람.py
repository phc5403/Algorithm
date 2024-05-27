from sys import stdin

N = int(stdin.readline())
res = set()
for n in range(N):
    # 사원과 출입상태를 저장
    people, state = list(stdin.readline().split())

    # 퇴근일 경우 삭제(문제 상 출근 없이 "leave"만 입력으로 들어오지 않아 고려할 필요 없음)
    if state == "leave":
        res.remove(people)
    else:  # 퇴근하지 않았다면 결과 목록에 추가
        res.add(people)

res = sorted(list(res), reverse=True)
print(*res, sep='\n')
