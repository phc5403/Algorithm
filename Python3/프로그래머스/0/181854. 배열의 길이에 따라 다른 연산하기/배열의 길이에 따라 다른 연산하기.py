def solution(arr, n):
    # answer = []
    length = len(arr)
    
    if length % 2 == 1:
        for i in range(0, length, 2):
            arr[i] += n
    else:
        for i in range(1, length, 2):
            arr[i] += n
            
    
    return arr