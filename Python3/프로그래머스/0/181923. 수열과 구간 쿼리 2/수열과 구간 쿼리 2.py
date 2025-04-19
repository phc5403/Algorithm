def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        candidates = [x for x in arr[s:e+1] if x > k]
        if candidates:
            result.append(min(candidates))
        else:
            result.append(-1)
    
    return result
