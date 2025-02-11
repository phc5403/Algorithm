def solution(my_string, m, c):
    answer = ''
    
    # 20
    # 0123 4567 8901 2345 6789
    # ihrh/bakr/fpnd/oplj/hygc
    #    3    7   11   15   19
    
    answer = ''
    for i in range(c-1, len(my_string), m):  # c-1을 기준으로 m 간격으로 선택
        answer += my_string[i]
                
    return answer