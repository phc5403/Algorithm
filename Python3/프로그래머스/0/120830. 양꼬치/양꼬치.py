def solution(n, k):
    answer = 0
    service = 0
    service = (int)(n / 10)
    k -= service
    
    answer = (n * 12000) + (k * 2000)
    
    return answer