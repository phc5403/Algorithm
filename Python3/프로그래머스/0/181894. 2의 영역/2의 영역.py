def solution(arr):
    start, end = 0, 0
    
    if 2 not in arr:
        return [-1]
    if len(arr) == 1 and arr[0] == 2:
        return [2]
    
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            break
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 2:
            end = i
            break
                        
    if end == 0:
        return arr[start]
    else:
        return arr[start:end+1]