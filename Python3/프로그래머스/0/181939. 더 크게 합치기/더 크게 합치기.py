def solution(a, b):
    answer = 0
    
    temp_a, temp_b = str(a) + str(b), str(b) + str(a)
    
    
    answer = max(int(temp_a), int(temp_b))
    
    return answer