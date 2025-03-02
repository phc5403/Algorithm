def solution(arr, idx):
    answer = 0
    
    for i in range(idx, len(arr)):
        if arr[i]:
            answer = i
            return answer
        
    answer = -1
    return answer