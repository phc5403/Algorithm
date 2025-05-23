def solution(my_string, n):
    answer = ''
    
    length = len(my_string)
    idx, cnt = 0, 0
    
    while idx < length:
        while cnt != n:
            answer += my_string[idx]
            cnt += 1
        
        if cnt == n:
            cnt = 0

        idx += 1
    
    return answer