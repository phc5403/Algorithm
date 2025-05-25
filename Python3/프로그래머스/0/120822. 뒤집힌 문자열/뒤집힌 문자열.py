from collections import deque


def solution(my_string):
    answer = deque(my_string)
    answer.reverse()
    
    return ''.join(answer)
    
    # answer = ''.join(answer)
    