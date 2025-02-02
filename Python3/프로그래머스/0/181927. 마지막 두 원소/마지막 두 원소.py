def solution(num_list):
    answer = num_list
    
    last_element = num_list[-1]
    last_front = num_list[-2]
    temp = 0
    
    if last_element > last_front:
        temp = last_element - last_front
        answer.append(temp)
    elif last_element <= last_front:
        temp = last_element * 2
        answer.append(temp)
    
    return answer