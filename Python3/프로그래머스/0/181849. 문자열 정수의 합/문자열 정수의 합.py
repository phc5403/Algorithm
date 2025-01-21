def solution(num_str):
    answer = 0
    num_str = list(num_str)
    
    for n in num_str:
        answer += int(n)
    
    return answer