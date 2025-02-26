def solution(n_str):
    idx = 0
    
    while 1:
        if n_str[idx] == '0':
            idx += 1
        else:
            break        

    return n_str[idx:]