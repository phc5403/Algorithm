def solution(my_string, overwrite_string, s):
    answer = []
    # my_string = list(my_string)
    # overwrite_string = list(overwrite_string)
    # print(my_string)
    # answer = my_string[:s] + overwrite_string[s:]
    
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    
    
    return answer
