def solution(my_string, letter):
    temp = [1] * len(my_string)
    answer = ''
    
    for ms in range(len(my_string)):
        if my_string[ms] == letter:
            temp[ms] = 0
            
    for t in range(len(temp)):
        if temp[t]:
            answer += my_string[t]
        
    return answer