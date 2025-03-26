import math

def solution(num_list):
    answer = 0
    length = len(num_list)
    
    if length > 10:
        answer = sum(num_list)
    else:
        answer = math.prod(num_list)
    
    
    return answer