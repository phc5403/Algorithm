def solution(l, r):
    # result = [num for num in range(l, r+1) if set(str(num)) <= {"0", "5"}]
    answer = []
    
    for n in range(l, r + 1):
        if set(str(n)) <= {"0", "5"}:
            answer.append(n)
    
    return answer if answer else [-1]
