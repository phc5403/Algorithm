def solution(array, n):
    answer = []
    temp = 0
    minValue = float('inf')
    
    for i in range(len(array)):
        temp = abs(array[i] - n)
        minValue = min(minValue, temp)

    for i in range(len(array)):
        if abs(array[i] - n) == minValue:
            answer.append(array[i])
        
    return min(answer)