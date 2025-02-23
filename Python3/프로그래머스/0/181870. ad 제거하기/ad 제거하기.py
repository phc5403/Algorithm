def solution(strArr):
    answer = []
    
    for idx in range(len(strArr)):
        if "ad" not in strArr[idx]:
            answer.append(strArr[idx])            
    
    return answer