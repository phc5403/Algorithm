def solution(my_string, queries):
    answer = list(my_string)
    
    
    for s, e in queries:
        temp = answer[s:e+1]  # [r, m]
        length = len(temp)
        
            
        for a, b in enumerate(range(length - 1, -1, -1), start = s):
            answer[a] = temp[b]        
        
    res = ""
    for r in answer:
        res += r
    
    return res
        