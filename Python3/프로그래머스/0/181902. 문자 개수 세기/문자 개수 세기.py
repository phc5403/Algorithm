def solution(my_string):
    # A-Z = 65 ~ 90 / a-z = 97 ~ 122 
    answer = [0] * 52
    
    for str in my_string:
        temp = ord(str)
        if 65 <= temp <= 90:
            answer[temp - 65] += 1
        else:
            answer[temp - 71] += 1
    
    
    
    return answer