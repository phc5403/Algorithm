def solution(s):
    answer = [0] * len(s)
    last_seen = {}
    
    for i, letter in enumerate(s):        
        if letter in last_seen:
            answer[i] = i - last_seen[letter]
        else:
            answer[i] = -1
            
            
        last_seen[letter] = i
    
    print(answer)
    
    return answer