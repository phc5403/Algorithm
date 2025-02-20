def solution(array, height):
    cnt = 0
    
    for a in array:
        if a > height:
            cnt += 1
            
    return cnt