def solution(t, p):
    answer = 0
    
    plen = len(p)
    idx = 0
    
    while idx + plen <= len(t):
        temp = t[idx : idx + plen]
        
        if int(temp) <= int(p):
            answer += 1
        
        idx += 1
    
    
    return answer