def solution(n):
    answer = 1
    cnt = 1
    
    while 1:
        # print(answer, cnt)
        answer *= cnt
        if answer <= n:
            cnt += 1
        else:
            return cnt - 1
    