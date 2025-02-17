def solution(my_string, s, e):
    answer = ''
    temp = ''
    
    reverse = my_string[s:e + 1]
    
    for i in range(len(reverse) - 1, -1, -1):
        temp += reverse[i]
    
    answer = my_string[:s] + temp + my_string[e + 1:]
    
    return answer