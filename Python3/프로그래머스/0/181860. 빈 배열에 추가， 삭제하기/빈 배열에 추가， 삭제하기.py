def solution(arr, flag):
    answer = ""
    length = len(answer)
    
    for i in range(len(flag)):
        if flag[i]:
            answer += str(arr[i]) * (arr[i] * 2)
        else:
            answer = answer[:length - arr[i]]
            
    
    length = len(answer)
    answer = list(answer)
    
    for i in range(length):
        answer[i] = int(answer[i])
    
    return answer