def solution(my_string):
    answer = []
    
    for n in my_string:
        if n.isdigit():
            answer.append(int(n))
            
    answer.sort()
    
    return answer