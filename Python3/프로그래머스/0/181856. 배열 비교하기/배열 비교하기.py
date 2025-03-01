def solution(arr1, arr2):
    answer = 0
    
    lrr1, lrr2 = len(arr1), len(arr2)
    
    if lrr1 > lrr2:
        answer = 1
    elif lrr1 < lrr2:
        answer = -1
    else:  # lrr1 = lrr2
        srr1, srr2 = sum(arr1), sum(arr2)
        
        if srr1 > srr2:
            answer = 1
        elif srr1 < srr2:
            answer = -1
        else:
            answer = 0
    
    return answer