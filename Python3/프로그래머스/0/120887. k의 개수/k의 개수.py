def solution(i, j, k):
    answer = 0
    
    for num in range(i, j + 1):
        num = list(str(num))

        for n in num:
            if int(n) == k:
                answer += 1
        
    return answer