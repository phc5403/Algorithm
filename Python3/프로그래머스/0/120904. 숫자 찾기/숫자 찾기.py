def solution(num, k):
    answer = -1
    num = str(num)
    k = str(k)
    
    for i in range(len(num)):
        if num[i] == k:
            answer = i + 1
            break
            
    return answer