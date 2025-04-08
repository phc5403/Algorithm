def solution(array):
    answer = 0
    
    for arr in array:
        for st in str(arr):
            if st == "7":
                answer += 1
    
    return answer